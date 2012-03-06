
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
    $ cd <base directory>/5Q
    $ mkdir GIT
    $ cd GIT
    $ git clone git@github.com:matiasherranz/5Q.git
    $ cd 5Q

