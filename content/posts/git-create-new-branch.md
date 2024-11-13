--- 
draft: true
title: "Git: create new branch"
date: "2021-09-08T15:42:13+0200"
layout: post
tags: ["git", "bash", "command line"]
slug: "git-create-new-branch"
---


How do you create a new branch from the command line?

If you are not on the main branch, go there first by typing:
```bash
$ git checkout main
Switched to branch "main"
```
Now you can create a new branch by doing:

```bash
$ git checkout -b issue40
Switched to new branch "issue40"
```

Imagine you fixed the issue and committed it to the "issue40" branch by

```bash
$ git commit -a -m "Fixed a bug [issue 40]"
```

You are now ready to merge the issue40 branch into the main branch. You can eitehr do this locally, or do it on Github.


