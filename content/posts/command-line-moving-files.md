--- 
draft: false
title: "Command line: moving files"
date: "2021-09-16T08:36:24+0200"
layout: post
tags: ["bash", "command line"]
slug: "command-line-moving-files"
---

Instead of litterring my site with small posts describing how to perform as certain task, I will devise a plan to really learning to master the command line. I have [a book about the command line](../books/the-linux-command-line.md), which can help to create an overview of what's there to learn about the command line.

Broader than just the command line, what do I want to learn? On the positive site, I have learned a lot and I keep learning new stuff. On the other hand, it is sometimes not very focused and, just like myself, all over the place. I don't know if that is a negative thing per se, or something I should change, but it would help me (I think) to make it easier to pick up where I have left sometimes.

So things I want to learn or even master are:
- command line
- git
- python
- django
- machine learning

OK, so let's get materials for each subject, link to them from the above list and add a "life long learning" tag to this post.

I need to add the command line book to my list of books. I also need to look up the script I used to extract all my books from Amazon. And in a broader perspective, I want to make sure I can always find code I have been working on. I have some code on my computer, somme of it is also on Github, how do I make sure everything slightly interesting can be found back, even when my computer crashes?

Another thing I want to change: I want to write everyday, I have set up a Hugo site, I have set up a script to create a new post from the command line, but I did make a mistake, as it turns out: I am asking for a title and some keywords *before I start writing*. I need to change this. I don't have to get rid of the script, it is still good for writing a post about a specific subject, but I need to cater for the daily writing. This only has to contain a date and a default title like "Daily writing" or so. These posts can have a default visibility of draft: true and some basis keyword(s) like "daily writing".

Now copying the script and alter it so it does that what I just desccribed is easy, for the short term. For the longer term, it is much better if I combine these options in the same script. For instance, leaving the title empty could then result in the daily post settings, or having the options to start different kind of posts or pages.

The pages I want to be able to create are:
- posts about specific topic
- daily writing posts
- project pages
- book page

The last one is probably easier to generate from a spreadsheet, I could/should/would alter the code so it actually reads directly from the generated CSV, although at the moment it is already working fine.

Let's assume I only want to provide for the first three options. I could show an options list [1], [2] and [3] as to what kind of post I would like to create. If it is a post about a specific topic or a project page, it would then ask for a title and keywords.

As for the project pages, I think I would like a set up where I have a 'startpage' for a project, with all posts with the 'project' and '[projectname]' tags shown underneath. As for the dates, I have decided not to include dates in the path, with Hugo I could even decide to change that some day.

So, different things to do:
- create a script with options
- create the projects section in Hugo


