--- 
draft: true
title: "Creating fixtures for testing Brede School"
date: "2021-09-14T10:24:07+0200"
layout: post
tags: ["testing","Brede School", "ToDo","django","fixtures"]
slug: "creating-fixtures-for-testing-brede-school"
---

We need fake content for the Brede School, and probably for other projects as well. This content is both needed for the Development environment as for testing purposes.

There are different methods to be used. I quite like the idea that we load the development environment with fake data, that we create from the command line (via a script).

This would mean generating schools, students, parents, teachers, schoolmanagers, companies, activities, schedules and participations (I might have forgotten something, but you get the gist, generate all necessary data).

An ideal package to take care of this, is by using [factory_boy](https://factoryboy.readthedocs.io/en/latest/).

Another solution is to use data from the live environment. How to do that?

