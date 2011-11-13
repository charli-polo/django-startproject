#!/usr/bin/env bash


# Make initial commmit
	cd PROJECT_ROOT
	git init
	git flow init
	git add .
	git commit -a -m 'initial commit'

# And now we can run !	
	bin/manage.py syncdb --migrate
	bin/manage.py runserver	

# Deploying the Project
# ======================

# On dotcloud:

# Copy dotcloud necessary files (AAA)
	cp server_configs/dotcloud/* .
	git add .
	git commit -a -m 'dotcloud files'