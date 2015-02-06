# KRONOS Lottery #

This is a Django application that is used to randomly choose participants for events.

### Install ###

Clone this repository:

    hg clone https://lmoppert@bitbucket.org/LEV_AppDev/lottery lottery/

Create a virtualenv:

    mkvirtualenv lottery

Install the required software:

    pip install -r requirements.txt
    
Create a database and user with your favorite management tool

### Configuration ###
Edit the `lottery/settings.py` to represent the database configuration. The password of the DB 
user should go into a file called `secrets.py` in the same directory where the `settings.py` file 
lives. Define the password as follow:

    DB_PASS = 'yor secret password'

After this, the management command should be able to communicate with the database. Now migrate:

    python manage.py migrate

And now you can start the development server:

    python manage.py runserver