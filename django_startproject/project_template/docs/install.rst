==================
Installation
==================

Pre-Requisites
===============

* `setuptools <http://pypi.python.org/pypi/setuptools>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_

To install all of these system dependencies on a Debian-based system, run::

	sudo apt-get install python-setuptools
	sudo easy_install virtualenv


Creating a local Dev Virtual Environment
================================

First, create a clean base environment using virtualenv::
    mkvirtualenv --no-site-packages SITE

Note: You can avoid the option if you don't want to "redownlaod" some heavy packages

Then, we install the django-start-project app:
	pip install -e ~/Dev/ressources/django-startproject/
	
We run the start-project to start a project (in the desired location)
	cd ~/Dev
	django-startproject.py Project_Root

We install the dependancies
	cd Project_Root
	pip install -r requirements.txt

FAUT IL INSTALLER LE PACKAGE POUR UTILSER manage.py ?
Ou cela a-t-il des effets nefastes (genre le truc dans le egg) ?
	
We copy the required files:
	local (from example if needed) -- A CREUSER...
	cd PROJECT
	cp conf/local/example/* conf/local/
	
And now we can run !	
	bin/manage.py syncdb --migrate
	bin/manage.py runserver

And then we can push


Deploying the Project
======================

On dotcloud:

Copy dotcloud necessary files (AAA)
	cp server_configs/dotcloud/* .

Create an instance and push
dotcloud create INSTANCE
dotcloud push


TO DO
======================
Ajouter la partie git... (git init)
Ajouter la partie git flow !
Comprendre comment gérer les fichiers de dotcloud (il ne devraient pas être copié en local cf AAA): script post dotcloud ?
Ajouter un test static (images)
DEGAGER les .DS_Store ...
REMETTRE une clé générée de façon aléatoire

SE POSER LA QUESTIN DES CONFS ...
Objectif: que ce soit versionné (c'est une bonne chose)
Pb: Sécurité (accès db)
Pb: Quid lors du dev en local... il faut utiliser dev tout le temps ?
exemple: bin/manage.py runserver --settings=PROJECT.conf.dev



NEXT
====
Lier à la créationd'un compte dotcloud (multi compte hook)







Install the requirements and the project source::

	cd path/to/your/myproject/repository
    pip install -r requirements.pip
    pip install -e .


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp myproject/conf/local/example/* myproject/conf/local
    manage.py syncdb --migrate


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    pip install Sphinx
    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
