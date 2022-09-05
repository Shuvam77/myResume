# Dynamic Resume
# Introduction
This is a simple digital dynamic resume project developed using Django Framework. This project can be used by anyone who wants to show their resume a digital format.

# Tech Stack
  1. [Python 3.9](https://www.python.org/)
  2. [Django 4.0.5](https://www.djangoproject.com/)
  3. [SQLite3](https://www.sqlite.org/index.html)
  4. [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/)
  5. [Bootstrap5](https://getbootstrap.com/)
  
# Installation
  **GIT clone from GitHub**
  
  ###### First step is to make a directory.
  ```
  $ mkdir myResume
  $ cd myResume
  ```
  
  ###### Then clone the [E-commerce App Repo](https://github.com/Shuvam77/myResume) from the GitHub.
  ```
  myResume $ git clone https://github.com/Shuvam77/myResume.git .
  ```
  
  **Python Enviornment**
  ###### Install and activate [Python virtual environments](https://docs.python.org/3/tutorial/venv.html). And activate it.
  ```
  myResume $ pipenv shell
  ```
  ###### or
  ```
  myResume $ python3 -m venv venv
  myResume $ source venv/bin/activate
  ```
  
  ###### Once it has been activated, install requirements.txt.
  ```
  (venv) myResume $ pip install -r requirements.txt
  ```
  
  **Start Migration**
  ###### Migration Process
  ```
  (venv) myResume $ python manage.py makemigrations
  (venv) myResume $ python manage.py showmigrations
  (venv) myResume $ python manage.py migrate
  ```
  
  ###### You can delete the current database db.sqlite3 file inside the main directory and start with clean database.
  
  ###### Create SuperUser
  ```
  (venv) myResume $ python manage.py createsuperuser
  
  Username: admin
  Email address: admin@email.com
  Password: sudo@123
  ```
  
  ###### Runserver
  ```
  (env) myResume $ python manage.py runserver
  ```
  
