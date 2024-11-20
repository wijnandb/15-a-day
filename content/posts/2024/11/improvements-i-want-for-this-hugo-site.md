--- 
draft: true
title: "Improvements I want for this Hugo site"
date: "2024-11-20T10:49:03+0100"
layout: post
tags: ["website", "todo", "hugo"]
slug: "improvements-i-want-for-this-hugo-site"
---

There is a number of things I would like to add and improve to this site.

One of the things I'd like, is to make the creation of a new post more seemless. I have created a shell script, with which I can create a new post. The script can be called from the command line:
```bash
$ ./new-post.sh
```

It creates a new file, in the directory posts/<YYYY>/<MM>/ with the title provided and the ".md" extension.
The settings for the file creation are hardcoded in the script, which is fine for now.

What I really like about the site, is that I writ in markdown yet the result is presented in a visually nice way. I also like the fact that I can navigate to related posts via the tags. In that sense, it is starting to become something of a second brain.

What I want to add/change:
- [ ] fix problem with links not working on [live version](http://www.baretta.nl)
- [ ] related posts (this is working for the books, but not for posts)
- [x] enable to see the draft posts as well when running locally

```bash
$ hugo server --buildDrafts
```
- [ ] add a footer
    - [ ] add most important tags to the footer
- [ ] on the tags page, I want to order the tags on frequency used, most important/most used on top
- [ ] Later: option to share articles via X, Mastodon, LinkedIn, et cetera.
- [ ] add search to the site
- [ ] add next/previous to navigation nderneath posts
- [ ] limit previous/next navigation under books to books (now includes the occassional post)
- [ ] limit size of "next" and "previous" images under books on mobile
- [ ] fix css for pagination icons. They look crappy, probably use same class for styling the books "next" and "previous"

### Enable drafts
The great thing about enabling drafts is that I can actually use this site fr note-taking without having to worry about whether I want to publish it or not. It also means I can use it as a ToDo list (by adding the tag "TODO" to it). Writing in markdown and getting a very nice visualization of my notes, really great!!




