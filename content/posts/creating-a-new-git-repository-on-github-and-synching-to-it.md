---
title: 'Creating a new Git repository on Github and synching to it'
date: 2021-08-31
layout: post
tags: ["git", "automation", "productivity", "tags"]
draft: false
---

I want to create a new Git repo and write down the commands to add new content or create a script which does that for me.

First, I go to the root directory of my (local) project and initiate a new Git repository:
```bash
$ git init
```
We now have an empty git repository. Add all files to it with
```bash
$ git add .
```

Setting up a repo on Github:
```bash
$ gh repo create project-name
```

I need to set the upstream branch on Github and get the .gitignore and the LICENSE that were  created when setting up the repo on Github:
repository:
```bash
$ git pull --set-upstream origin main
```
On Github, the default branch is called main, which I also want in my local repository:
```bash
$ git branch -m master main
```

Now push the changes from the local repo to [Github]. 

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   posts/2021-08-31-creating-a-new-git-repository-on-github-and-synching-to-it.md

no changes added to commit (use "git add" and/or "git commit -a")

$ git add posts/2021-08-31-creating-a-new-git-repository-on-github-and-synching-to-it.md 

$ git commit -m "Update post"
[main 54bc05a] Update post
 1 file changed, 12 insertions(+), 7 deletions(-)

$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 600 bytes | 600.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/wijnandb/15-a-day.git
   3538963..54bc05a  main -> main
```

Good, the contents of the local changes have been pushed to the Github repository, ready to be published.

Slightly distracted for a while, publishing the site on [Github] with one of the default themes, the [Minimal theme]. 

Quite happy already and realising myself that tweaking the theme is about the stupidest thing I can do at the moment, given the reason for setting this up is to write everyday, not loose myself in working on yet another static site.

So, that's it for now, I have been pushing changes via the command line, as I should. 

If I keep writing content, I will make changes to this layout/theme. Chnages I will be making are, among others:
- create a tags page
- add links to tags (so you see other pages with that tag)
- move tags up, under the title
- make the right column a bit wider
- center align the logo in the left column

That's it for now. So I'll go to my bash shell and type:
```bash
$ git status
$ git add .
$ git commit -m "Update post"
$ git push
```



[Github]: https://github.com
[Minimal theme]: https://github.com/pages-themes/minimal
