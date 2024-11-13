--- 
draft: true
title: "Setting up a new Django project"
date: "2021-12-20T14:06:02+0100"
layout: post
tags: ["django","howto","notes"]
slug: "setting-up-a-new-django-project"
---

I have looked into Cookiecutter, as a way to create new Django projects. 

Problem is that I still haven't mastered working with Virtual Environments.

I am using Pipenv instead, which works fine, but I don't really understand how it works. Besides that, it isn't actively maintained, which is a problem.

So, venv. 

Questions:

1. Which Python version is being used on Heroku?
   - 3.10.1
   - Locally installed that version as well, Python3.10
2. Which Django version can be run on Heroku?
3. Which Postgres version can be run on Heroku?
4. How can I choose between different versions of Python locally?

Well, this little exercise has gotten me in all kinds of shit. I can't get my existing Django projects to run locally, I have really messed up.

I tried getting an existing Django project running with venv, which didn't work. For some reason my .env variables weren't loaded, and I haven't been able to figure out why that is. It might have to do with the creation of an "env" directory. Deleting it didn't solve the problem though. 
