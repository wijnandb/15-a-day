--- 
draft: true
title: "Bredeschool ToDo: activity views"
date: "2021-09-09T13:43:16+0200"
layout: post
tags: ["ToDo", "brede school",]
slug: "bredeschool-todo-activity-views"
---


There are different views to show activities, different ones for each type of user:

- visitor
- parent
- teacher
- schoolmanager

Ideally, we subclass the views to show all users the right set of activities. By subclassing, we can not only change the filtering, we can also assign different templates for different users.

So, how do we get this done?

First of all, let's define the different views, determine who can see them and what is different about them.

Let's just start with the URL's we'll figure out the rest later.


[Visitors: http://127.0.0.1:8000/activity/](http://127.0.0.1:8000/activity/)

[Parents: http://127.0.0.1:8000/parent/student/enrollment/2354/](http://127.0.0.1:8000/parent/student/enrollment/2354/)

[Teacher: http://127.0.0.1:8000/teacher/teacher/dashboard/](http://127.0.0.1:8000/teacher/teacher/dashboard/)

[Schoolmanager: http://127.0.0.1:8000/schoolmanager/activities/1/](http://127.0.0.1:8000/schoolmanager/activities/1/)





# Show only current activities

We need to filter on Schedule. How do you determine what the "active" Period is?
I could get the latest (=highest id) or set it explicitly in the SETTINGS.
Done. In settings we now have a CURRENT_PERIOD which is set to the id that we want as a CURRENT_PERIOD. Everything for users other than Supermanagers are filtered on this.

