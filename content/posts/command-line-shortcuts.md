--- 
draft: false
title: "Command line shortcuts"
date: "2021-10-08T08:12:29+0200"
layout: post
tags: ["bash", "scripts","productivity"]
slug: "command-line-shortcuts"
---

Why not create shortcuts/shell scripts to open a project, similar to the script to create a new post?

I could make it so that if I want to open a project, I cd into the directory belonging to the project, activate the environment and start up a server. 
I could even make it so that all projects start a server on their own port, so multiple projects could have a simultaneously running server.


So typing ```` $ bredeschool ````

would cd into the directory /home/wijnandb/sites/heroku/bredeschool
```` $ cd /home/wijnandb/sites/heroku/bredeschool ````

Then activate the enviromnent by running 
```` $ pipenv shell ````

and finally spin up a server by running 
```` $ python manage.py runserver localhost:8000````