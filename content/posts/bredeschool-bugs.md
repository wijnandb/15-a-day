--- 
draft: true
title: "Bredeschool bugs"
date: "2021-09-08T11:13:36+0200"
layout: post
tags: ["project", "brede school", "ToDo", "notes", "private"]
slug: "bredeschool-bugs"
---

There are a number of bugs to be solved in the Bredeschool project. To work on them effectively, I need structure. And to get thta structure, I'll start describing the bug and the way I want to fix that bug.

### Children are not added to the Parent's account
If a parent creates an account, there is a check (via a signal) if there are children who are listed with the same e-mail address. If that is the case, the child is added to the parent's account, so they see their child when they login. This works fine, unless the casing of the e-mail address is different, for innstance if one of addresses contain uppercase letters.

Proposed solution:
- both addresses can contain capitols
- lowercasing the parent address when checking
- lowercasing the child addresses when importing.

#### How can we check?
Lowercasing the parent address when checking has been implemented. 
- <strike>add lowercased address to student</strike>
- <strike>create new account for parent containing UPPERCASED letters</strike>
- check if child is added to newly created account

Perfect, this one works, can be put live.

#### Lowercasing the child addresses on import
During the import, when the emial addresses are addded, lowercase them.

#### Check if it works
- create an upload CSV containing addresses with uppercase letters
- upload the file
Unfortunately, this gives an error:
```python
ERROR: 'NoneType' object has no attribute 'lower'
```

Problem is that it fails when there is no emailaddress. Fixed it, it works.

- check if letters have been lowercased

Yes, they are.

- check if parent with same address/different casing has been added

No. This is because of the order of events. There is a check when a new parent account is created, and there is a check when a new student account has been created.

I don't know how to fix this, I'm leaving it open. This means that if new students are uploaded and their parent's email address contains upercase letters, the child will not be added to the parent's account.

# ToDo
A way to solve this is to update the registered e-mail addresses, set them all to lowercase. I also want to update the Usernames, set them to the mailaddress. I need to check if there is a conflict if I do so, so check if an emailaddress exists more than once.

Or, when someone creates a new account, only allow lowercase.


### Allauth Settings 
[ACCOUNT_AUTHENTICATION_METHOD (=”username” | “email” | “username_email”)](https://django-allauth.readthedocs.io/en/latest/configuration.html)

### Layouts in the /templates/account/ section are not displaying as they should



### Automatic placement algorithm not working as it should

## Performance:

### Requesting page with Children from school takes ages

- Only show one school
- 
