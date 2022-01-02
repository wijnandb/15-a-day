---
title: 'Creating a new post from the command line'
date: 2021-08-31
layout: post
tags: ["productivity", "bash", "automation", "tags"]
draft: false
---

Ok, that worked. I can now create new posts from the command line by simply calling the bash script I have created. 
Calling ./new-post.sh asks for a title and keywords (tags) and creates a new post for me in the desired directory (~/15-a-day/posts).

This is a good beginning, there are however some steps left. First, let me document what I have created by adding the contents of the bash script to this post.

To do this, I need another scipt or, seeing that I will only use this once, a couple of commands to paste and execute on the command line.

```bash
#! /bin/bash/

THIS_POST=${HOME}/15-a-day/posts/2021-08-31-let-us-see-if-this-works-creating-a-new-post-from-the-command-line.md
SCRIPT=${HOME}/15-a-day/new-post.sh

cat "$SCRIPT" >> "$THIS_POST"

```
And boom here it is:


```bash
#!/bin/bash

echo "The name of today's post"
read title

echo "Give the tags you want to include"
read tags

posttitle="$(echo -n "${title}" | iconv -t ascii//TRANSLIT | sed -r s/[^a-zA-Z0-9]+/-/g | sed -r s/^-+\|-+$//g | tr A-Z a-z)"

echo "Converted title of post is:"
echo "$posttitle"

today=`date +%Y-%m-%d`

timestamp=`date '+%Y-%m-%d %H:%M:%S'`


opslaan="${today}-${posttitle}"

filename="${HOME}/15-a-day/posts/${opslaan}.md"

echo "Creating file: ${filename} on ${today}"
echo "with title ${title} and tags: ${tags} and content: "

touch "$filename"


echo "---" >> $filename
echo "title: $title" >> $filename
echo "date: $timestamp" >> $filename
echo "
echo "tags: $tags" >> $filename
echo "draft: true" >> $filename
echo "---" >> $filename
echo >> $filename
echo "Well done! Start writing some content!" >> $filename
echo >> $filename

code "$filename"
```

A quick walk-through so I'll understand it when I need it somewhere in the future:
- first, script asks for a title, which is the normal, human readable title
- then, it asks for tags, which can be given in comma-seperated form
- it then *slugifies* the title, turning it lowercase and replacing any none alphanumeric characters with hyphens, to use in the name of the file
- then it gets the date, aslso to use in the name of the file
- it constructs the filename by combining the right directory with the date and the *slugified* title
- in the *metadata* for the markdown, it use the human-readable title, the date and time, adds the *tags* and sets *draft* to true, meaning the file won't be published.
- finally, it opens the file in my text-editor of choice, Visual Studio Code

Well, this is certainly a good start. Now, as I have mentioned before, I need to make sure nothing gets lost. This means version control with Git and creating a repository on Github to push to it.

Because I need to master this kind of operations, I will create a new post explaing the steps. As an added benefit, I need to find out how to create a link to another post. Square brackets around the name of the link, parentheses around the link itself.

[Read about creating a Git repo on Github and synching to it]({{< ref "/posts/creating-a-new-git-repository-on-github-and-synching-to-it" >}} "Creating new git repo")


