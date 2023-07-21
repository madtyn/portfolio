# portfolio
This is a personal portfolio for getting together my main Python projects and source code for recruiters.


### How to run

Just like any Django project:

python manage.py runserver [<ip>:port]

### How to update i18n texts and strings

#### Updating one language
django-admin makemessages -l en

#### Updating all languages
django-admin makemessages -a

#### Compiling all into *.po
django-admin compilemessages
