---
title: 'Create post via shell script'
date: 2021-08-31
layout: post
author: wijnandb
tags: ["shell", "linux", "static sites", "markdown", "automation", "tags"]
draft: false
featuredImage: "/images/foggy_mountain.jpg"
---

I want to write posts via the command line and I want it to be as effortless as possible.
Every time I want to start writing, I end up in a loop:

- let's create a site to publish my writing
- what are the possibilities?
- Django or static site?
- which static site generators are there?
- This one's nice!
- it's perfect for what I want
- can I change the theme/templates?

After a while, I have yet another nice static site. Sometimes all the way down to a published site, sometimes stuck somewhere half-way.  But all of the time, the writing of content stops, doesn't get started, never happens. No matter what the reason for this is, I need to get out of this loop.

So, I figure (not) writing has the do with the desire to write, combined with the effort it takes. Desire has to be greater than effort for it to happen. The equation is slightly more complicated, but this simple version will work for now. So, either increase the desire or decrease the effort.

Now, given the fact that all the static sites I keep making are build upon markdown files, that's the format they will have. I have been reading about the possibilities oif the commnad line on Linux and I have decide that I will use that to create posts. One of the problems I encountered was that I hate having to write the metadata for the markdown of a post. Especially the fact thta I need to type the date really pisses me of and results in me just refusing to do it. 

So, I write in all kinds of places, never being able to find anything back, pretty frustrating.

So, to remedy this, I want a script that I can run, which asks for a title, maybe some keywords (tags) and a category, that will produce and open a new post.

In my opinion that would make it more easy for me to create content, whether it is just little notes (reminders), or insicghts about how to program something, or a review for a book, let it be small and effortless.

There are some other concerns as well:

- I don't want to loose any content when my computer crashes
- I would like to be able to publish some stuff someday
- I don't want all my stuff to become available to everyone automatically

So, in order to achieve that, I will have git in place (keeping track of any changes) and I will have a (private) Github repository to sync data to. Ideally, I will have either the commmands written down/remembered to puish changes to the Github repository, or I wil have a script that does it for me.

OK, a script that generates a new post for me, with the metadata for the markdown file already filled out. 

The scenario for this script is something like this:

- run script
- asks for a Title
- creates a file based on that title
- fills the content of the file metadata
- creates/saves the file
- opens the file in an editor

The metadata will consist of:


```markdown
---
title: The title of the post as filled out by the user
date: DD/MM/YYYY HH:MM
tags: optional tags as filled out by user
category: optional category as filled out by user, defaults to "15 a day"
draft: True
---
```

#### 2024 Update: 
Done.
I can open a terminal and type 
```bash
$ new-post.sh
```

The script will run, no matter from where I call it. It will ask for a title, then for some tags (optional). It will create a new post, store it in the right directory (to be able to keep an overview it will store it in content/posts/YYYY/MM/).
It will then open the file in VS code and I can start writing.

Boom! :fire:


