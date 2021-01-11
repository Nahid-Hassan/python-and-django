# Django at a glance

Because Django was developed in a fast-paced newsroom environment, it was designed to make common Web-development tasks fast and easy. Here’s an informal overview of how to write a database-driven Web app with Django.

## Design your model

Although you can use Django without a database, it comes with an object-relational mapper in which you describe your database layout in Python code.

The data-model syntax offers many rich ways of representing your models – so far, it’s been solving many years’ worth of database-schema problems. Here’s a quick example:

`mysite/news/models.py`:

```py
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

## Install it

Next, run the Django command-line utilities to create the database tables automatically:

```console
root@admin: ~$ python manage.py makemigrations
root@admin: ~$ python manage.py migrate
```

## Enjoy the free API

```py
# Import the models we created from our "news" app
>>> from news.models import Article, Reporter

# No reporters are in the system yet.
>>> Reporter.objects.all()
<QuerySet []>

# Create a new Reporter.
>>> r = Reporter(full_name='John Smith')

# Save the object into the database. You have to call save() explicitly.
>>> r.save()

# Now it has an ID.
>>> r.id
1

# Now the new reporter is in the database.
>>> Reporter.objects.all()
<QuerySet [<Reporter: John Smith>]>

# Fields are represented as attributes on the Python object.
>>> r.full_name
'John Smith'

# Django provides a rich database lookup API.
>>> Reporter.objects.get(id=1)
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__startswith='John')
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__contains='ith')
<Reporter: John Smith>
>>> Reporter.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Reporter matching query does not exist.

# Create an article.
>>> from datetime import date
>>> a = Article(pub_date=date.today(), headline='Django is cool',
...     content='Yeah.', reporter=r)
>>> a.save()

# Now the article is in the database.
>>> Article.objects.all()
<QuerySet [<Article: Django is cool>]>

# Article objects get API access to related Reporter objects.
>>> r = a.reporter
>>> r.full_name
'John Smith'

# And vice versa: Reporter objects get API access to Article objects.
>>> r.article_set.all()
<QuerySet [<Article: Django is cool>]>

# The API follows relationships as far as you need, performing efficient
# JOINs for you behind the scenes.
# This finds all articles by a reporter whose name starts with "John".
>>> Article.objects.filter(reporter__full_name__startswith='John')
<QuerySet [<Article: Django is cool>]>

# Change an object by altering its attributes and calling save().
>>> r.full_name = 'Billy Goat'
>>> r.save()

# Delete an object with delete().
>>> r.delete()
```

*A dynamic admin interface: it’s not just scaffolding – it’s the whole house*:

`mysite/news/admin.py`

```py
from django.contrib import admin

from . import models

admin.site.register(models.Article)
```

## Design your URLs

A clean, elegant URL scheme is an important detail in a high-quality Web application. Django encourages beautiful URL design and doesn’t put any cruft in URLs, like .php or .asp.

To design URLs for an app, you create a Python module called a `URLconf`. A table of contents for your app, it contains a mapping between URL patterns and Python `callback` functions. `URLconfs` also serve to decouple URLs from Python code.

Here’s what a `URLconf` might look like for the Reporter/Article example above:

`mysite/news/urls.py`

```py
from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
```

For example, if a user requested the URL `“/articles/2005/05/39323/”`, Django would call the function

```py
news.views.article_detail(request, year=2005, month=5, pk=39323).
```

## Write your views

Each view is responsible for doing one of two things: Returning an `HttpResponse` object containing the content for the requested page, or raising an exception such as `Http404`. The rest is up to you.

Generally, a view retrieves data according to the parameters, loads a template and renders the template with the retrieved data. Here’s an example view for year_archive from above:

```py
from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```

## Design your templates

The code above loads the **news/year_archive.html** template.

Django has a template search path, which allows you to minimize redundancy among templates. In your Django settings, you specify a list of directories to check for templates with **DIRS**. If a template doesn’t exist in the `first directory, it checks the second, and so on`.

Let’s say the `news/year_archive.html` template was found. Here’s what that might look like:

`mysite/news/templates/news/year_archive.html`

```html
{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
```

`Variables` are surrounded by `double-curly braces`. `{{ article.headline }}` means `“Output the value of the article’s headline attribute.”` But `dots` aren’t used only for `attribute lookup`. They also can do `dictionary-key` lookup, `index lookup` and `function calls`.

Note `{{ article.pub_date|date:"F j, Y" }}` uses a `Unix-style “pipe” (the “|” character)`. This is called a `template filter`, and it’s a way to filter the value of a variable. In this case, the date filter formats a Python datetime object in the given format (as found in PHP’s date function).

You can `chain together as many filters` as you’d like. You can write `custom template filters`. You can write `custom template tags`, which run custom Python code behind the scenes.

Finally, Django uses the concept of `“template inheritance”`. That’s what the `{% extends "base.html" %}` does. It means `“First load the template called ‘base’, which has defined a bunch of blocks, and fill the blocks with the following blocks.”` In short, that lets you dramatically cut down on redundancy in templates: each template has to define only what’s unique to that template.

Here’s what the “base.html” template, including the use of static files, might look like:

`mysite/templates/base.html`

```html
{% load static %}
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <img src="{% static 'images/site-logo.png' %}" alt="Logo">
    {% block content %}{% endblock %}
</body>
</html>
```

- [Cache](https://docs.djangoproject.com/en/3.1/topics/cache/)
- [RSS Feed](https://docs.djangoproject.com/en/3.1/topics/cache/)
