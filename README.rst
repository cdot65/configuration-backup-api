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


Docker Deployment
^^^^^^^^^^^^^^^^^

Docker is available for local deployment, it is not currently setup for a production environment. Please let me know if you'd be interested in such a concept, or just stick with a standard Django install found below.

* Run the web application::

    $ docker-compose up -d 

* Create the database migrations for the backup app::

    $ docker-compose run web python manage.py migrate backup 

* Create the database migrations for the actual app::

    $ docker-compose run web python manage.py migrate 

* Create a superuser::

    $ docker-compose run web python manage.py createsuperuser

* Access in your web browser at `localhost:8000`

* Log in with your superuser account at `http://localhost:8000/api-auth/login/?next=/`


Local Deployment
^^^^^^^^^^^^^^^^

Follow this excellent guide here: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04


Basic Commands
--------------

This is a Python Django web application, so the commands you'll be using to manage this application will feel at home if you're familiar with working in this framework.


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

