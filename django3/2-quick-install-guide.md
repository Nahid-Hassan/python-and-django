# Quick install guide

Before you can use Django, you’ll need to get it installed.

## Install Python

Being a Python Web framework, `Django` requires `Python`.

```console
root@admin: ~$ sudo apt install python3.8
root@admin: ~$ python3 --version
```

## Set up a database

This step is only necessary if you’d like to work with a “large” database engine like **PostgreSQL**, **MariaDB**, **MySQL**, or **Oracle**. To install such a database, consult the database installation information.

## Install Django

```console
root@admin: ~$ python -m pip install Django
root@admin: ~$ python
>>> import django
>> print(django.get_version())
3.1
```

