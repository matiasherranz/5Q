
Welcome!

In this file I describe how to setup and run the Django project.


1. Setup the environment
###############################################################################

As I work on many projects, it becomes quite necessary and suitable to user
virtualenv. I created the app inside a virtualenv.

How to create it and run the project? Follow this simple steps:

Note: I use Python 2.7.2. You can also use 2.6.

    - If you don't have virtualenv installed:
        $ sudo easy_install virtualenv

    - Create the virtualenv:
        $ mkdir -p <base directory>/5Q
        $ cd <base directory>/5Q
        $ virtualenv --no-site-packages --distribute --python=python2.7 Env

Now you have the virtualenv created. Let's activate it and install the project
dependencies:
    $ source Env/bin/activate
    $ pip install -r GIT/docs\ and\ setup/pip-requirements.txt


2. Checkout the GIT repo
###############################################################################

I created a repo in GitHub and put the code in it.

To checkout the code, go this way:
    $ cd <base directory>
    $ mkdir 5Q
    $ cd 5Q
    $ mkdir GIT
    $ cd GIT
    $ git clone git@github.com:matiasherranz/5Q.git
    $ cd 5Q


3. Sync the database
###############################################################################

I created a setup using an SQlite3 database. To sync the database, run this
command:
    $ python manage.py syncdb

Note: in the db I uploaded to the repo, the admin username is 'admin' and
      the password is 'admin'


4. User registration settings
###############################################################################

As I had some extra time, I also implemented user registration.

It need some setup(in settings.py).

In order to signup mails to be sent, give proper values to this variables
in your settings.py file:
(this example is to use a Gmail address for mail sending)

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'USER@YOUR_DOMAIN.com'
    EMAIL_HOST_PASSWORD = 'YOUR_PASS'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

Or go this way if you prefer to use a local dev mail server:

    - In a terminal(appart from the one with the Django runserver), run this:
            $ python -m smtpd -n -c DebuggingServer localhost:1025

    - And set this in your setings.py:
            EMAIL_HOST = 'localhost'
            EMAIL_PORT = 1025


5. Run the app
###############################################################################

Just go to:
    $ cd <base directory>5Q/GIT/5Q/code/FiveQTest

And run the command:
    $ python manage.py runserver
