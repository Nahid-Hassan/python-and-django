# Writing your first Django app, part 1¶

Let’s learn by example.

Throughout this tutorial, we’ll walk you through the creation of a basic poll application.

It’ll consist of two parts:

- A public site that lets people view polls and vote in them.
- An admin site that lets you add, change, and delete polls.

We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):

```console
root@admin: ~$ python -m django --version
```

## Creating a project

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of `settings` for an instance of `Django`, including `database configuration`, `Django-specific options` and `application-specific` settings.

From the command line, cd into a directory where you’d like to store your code, then run the following command:

```console
root@admin: ~$ django-admin startproject mysite
root@admin: ~$ cd mysite
root@admin: ~$ ls mysite
manage.py mysite/
root@admin: ~$ python manage.py runserver
.............
Starting development server at http://127.0.0.1:8000/
.............
```

**Changing the port**:

```console
root@admin: ~$ python manage.py runserver 8080 # port number
# or
root@admin: ~$ python manage.py runserver 0:8080 # 0 for localhost 0.0.0.0 and 8080 is a port number
```

**Note**: Runserver is automatically reloading.

```console
root@admin: ~$ python manage.py startapp polls
```

**Projects vs. apps**:

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

## Write your first view

Let’s write the first view. Open the file `polls/views.py` and put the following Python code in it

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

This is the `simplest view` possible in Django. To call the view, we need to map it to a `URL` - and for this we need a `URLconf`.

To create a URLconf in the `polls` directory, create a file called `urls.py`. Your app directory should now look like.

```console
root@admin: ~$ ls
db.sqlite3  manage.py  mysite  polls
root@admin: ~$ cd polls
root@admin: ~$ ls
__init__.py  admin.py  apps.py  migrations  models.py  tests.py  views.py
root@admin: ~$ touch urls.py
```

In the **polls/urls.py** file include the following code:

```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

The next step is to point the `root URLconf` at the `polls.urls` module. In `mysite/urls.py`, add an import for `django.urls.include` and insert an `include()` in the urlpatterns list, so you have

`mysite/urls.py`:

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

The `include()` function allows referencing other URLconfs. Whenever Django encounters `include()`, it `chops off` whatever part of the URL matched up to that point and `sends the remaining string to the included URLconf for further processing`.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

**When to use include()**:

You should always use **include**() when you include other URL patterns. **admin.site.urls** is the only exception to this.

**path()**:

Signature: path(`route`, `view`, `name`, `kwargs`)
