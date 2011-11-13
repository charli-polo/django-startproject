#!/usr/bin/env bash

# Make initial commmit
	git init
	git flow init
	git add .
	git commit -a -m 'initial commit'

# Deploying the Project
# ======================

# On dotcloud:

# Copy dotcloud necessary files (AAA)
	cp server_configs/dotcloud/* .
	git add .
	git commit -a -m 'dotcloud files'
	
	
# And now we can run !	
	# python myproject/bin/manage.py syncdb --migrate
	# python myproject/bin/manage.py runserver	
