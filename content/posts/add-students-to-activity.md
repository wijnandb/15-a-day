--- 
draft: true
title: "Add Students to activity"
date: "2021-09-10T08:14:57+0200"
layout: post
tags: ["brede school", "done", "notes", "ToDo"]
slug: "add-students-to-activity"
---


Op live omgeving is Leerlab rekenen voor Shri Laksmi een interne activiteit, Id= 246, het is op vrijdag om 14:45

OK, so it is actually a different problem. For "internal activities", we need to add all children as "Interested" to the activity.

How are we going to do that?

First, totally besides this problem, we need to see if some importnat changes won't break on live. So we deploy the branch with those changes [rqrmnts](https://github.com/wijnandb/bredeschool/tree/rqrmnts). If no-one complains, we merge rqrmnts with master. If there are problems, we deploy master.

So, we need to find a way to add all children from the group(s) an activity is for to the activity.

In pseudocode this would be like:

- trigger (this can be when activity is set to internal activity, or button a schoolmanager pushes, or as part of auto-placement)
- loop over groups the activity is for (only for current school)
- loop over students per group
- add record to Participation, with student, schedule and status=1


Page is [schoolmanager/activiteit/3620](http://127.0.0.1:8000/schoolmanager/activiteit/3620/)

View is ScheduleParticipantsView.

Now only showing when activity is set to "Internal activity". Shouldn't we show this all of the time?
