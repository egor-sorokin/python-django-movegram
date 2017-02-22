# python-django-movegram

## Instalation
Make a clone of this repository or download ZIP.

If you don't have python/pip/Django or Pillow pre-installed, you can use official docs: 
  - https://www.python.org/downloads/
  - https://pip.pypa.io/en/stable/installing/
  - https://docs.djangoproject.com/en/1.10/topics/install/
  - http://pillow.readthedocs.io/en/3.4.x/installation.html
  
If you already have python on your machine, the installation of other tools will be low-hanging fruit for you, just type in your terminal:
```sh
$ python get-pip.py
$ pip install Django
$ pip install Pillow
```

**Note**: If the permission is denied for you, it can be fixed by the command `chown` (please read more about that in the Internet) or just use `sudo` like that:
```sh
$ sudo pip install Django
$ sudo pip install Pillow
```

## Run server
In your terminal type:
```sh
$ cd [project-dir]
$ python manage.py migrate
$ python manage.py runserver
```
By default you can find the app on http://127.0.0.1:8000/

## Existing user and access
http://127.0.0.1:8000/login/

username: egorsorokin  
password: egorsorokin

## Access to the admin panel
http://127.0.0.1:8000/admin

username: egorsorokin  
password: egorsorokin
