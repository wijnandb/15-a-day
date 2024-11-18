---
draft: false
title: V-Bucks explained
date: "2021-09-16T09:59:24+0200"
layout: post
tags: ["project", "v-bucks"]
slug: "a-post-about-vbucks"
---
November 2024 update. Read below for the idea of V-bucks.
Revisiting this old post, I ask ChatGPT to help: https://chatgpt.com/share/67351ff2-8f14-800a-a499-0120b9518c78 

This is still an interesting and nice idea to build a MVP for.


The V-Bucks project (or better yet, in this phase: idea) has originated at home, because my sons would like to earn money (to spend on V-bucks, the virtual currency used in Fortnite) and I would like them to do some chores in and around the house.

The idea is that, because teens seem to forget about everything except checking their phone, we would create a little app which would show which chores there were to be done and the amount of V-Bucks to be earned by doing them.

There were "son-specific" chores and there were "open chores", the first to do the chore would earn the V-Bucks. Recurring chores, epic chores, all kinds of ideas floated around. 

The underlying thought was that they would create a habit of doing certain things. It is basically a way of determining the amount of your pocket-money, while helping out your mom and dad, developing some good habits along the way. And because we figured the same problem would be experienced by other parents, why not try to solve this for all of us.

We started out "low-tech", just a list on paper where chores could be claimed. Then we moved to a spreadsheet and a form. It clearly worked, so it is time to move on and create a Minimum Viable Product (MVP)[^1].

Since I like working with Django, that is the goto platform to develop this on. 

A login functionality will be needed, but this is baked into Django, so that's taken care of. Once a user logs in, they see their chores that are due. We will use a push mechanism to push new chores, so if all chores (for that moment) are done, something nice will be shown (a random cat or something) with a text saying "You are all done!".

Chores have a status ("open" or "done") and an optional timestamp. 

To make it easy, and probably the best solution for an MVP, we have a due_tasks table, which contains the tasks that are due for each user. So it contains user, task, start and end (where start is the first moment a chore can be done and end is the deadline for when a certain chore can be done).

A page for a user is a simple ListView filtered on User and datetime between "start" and "end". 
The page has the option to mark the task as "done". 

- Do we want to include some proof that a task has been done? 
- Or the ability for the admin/parent to approve or disapprove a fulfilled task?
- nice to have: option to add a photo (show photo icon. When clicked: opens camera. When taken a photo, option to add text and send) 
  - maybe use an existing service for this, like Telegram

What about using the Telegram interface? Send a task when it's due, like "make your bed". Option to reply, when received, bot sends something nice, creating a little *feel-good moment*.
If no reply, re-send an hour before task-window closes.

More difficult to deal with tasks that are aimed at more than one person, although what we could do, is just let it dissapear when it is done by someone. That would also mean that having a Javascript powered website more suitable.



Interesting ideas:
- [Use a Telegram bot](https://core.telegram.org/bots)

[^1]: Technically we already had a MVP with the spreadsheet and the form, it's just that I want to avoid "going under water" to build an extended version without simultaneously using and therefore testing it. 
