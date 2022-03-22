# AutodeskServices
###### This is a Django app, which uses sqlite3

### When using PyCharm

When we open a project with a requirements file, PyCharm detects this and offers to create a virtual nvironment and automatically install the dependencies.

### When using VScode

First of all, go to "Extensions" (Ctrl+Shift+X) and for Python support you should install Python extension by Microsoft. After you install the extension, open the project, and from the bottom left corner create an environment.

####

Basic commands to make the app work:
-navigate to the folder where you can find manage.py and:

* python manage.py runserver * - *this command starts the server - http://127.0.0.1:8000/*

commands related to database:
* python manage.py showmigrations *
* python manage.py makemigrations *
* python manage.py migrate * 
