Pinecone Configuration Backup API
=================================

.. image:: pinecone.svg

codename: Ralph

.. image:: https://img.shields.io/badge/code%20style-loose%20ferrets-brightgreen
     :target: https://www.youtube.com/watch?v=DwQ4xLdOIbM
     :alt: Ferret code style


:License: MIT


Deployment
----------

The following details how to deploy this application.



Local Deployment
^^^^^^^^^^^^^^^^

* To build the database changes::

    $ python manage.py makemigrations

* Apply the database changes::

    $ python manage.py migrate

* Create a superuser::

    $ python manage.py createsuperuser

* Run the web server::

    $ python manage.py runserver 0.0.0.0:8000

Docker Deployment
^^^^^^^^^^^^^^^^^

Docker is currently under development

Basic Commands
--------------

This is a Python Django web application, so the commands you'll be using to manage this application will feel at home if you're familiar with working in this framework.


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

