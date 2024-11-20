--- 
draft: false
title: "My static Hugo site: ToDo list"
date: "2021-09-07T09:24:42+0200"
layout: post
tags: ["todo", "hugo", "static site", "CDN"]
slug: "my-static-hugo-site-todo-list"
featuredImage: "/images/foggy_mountain.jpg"
---

OK, I have my HUgo site running locally and it is working fine. The script I have created to [create new posts from the command line]({{< ref "/posts/create-post-via-shell-script" >}}) is also very nice. No need to cd into any directory, just type ```bash $ new-post.sh ```, give a name and some tags and my new post is created and my editor is opened with that post, with the frontmatter in place.

The site is looking good, I'm happy with it, there are however some things I'd like to do to improve it further.

- [ ] Host it somewhere. Github or S3, doesn't really matter.
- [ ] Auto sync it. There is no script in place to do add files to git, commit the changes and push it to Github. 
  - [ ] Create a publish-hugo.sh script which does the following:
    - [ ] add all files to Git
    - [ ] create a commit message 
            ```
            $ git commit -m "New post: `date +'%Y-%m-%d %H:%M:%S'`" # New post: 2021-09-07 11:26:58
            ``` 
    - [ ] Alternative: add commit message while calling the script:
      - [ ] 
- [ ] Create a Medium profile. Since I'm starting to write, I might as well publish on some reading platform
- [ ] Spellingcheck posts and pages. It makes no sense to automate things and leave out spell-checker
  - [ ] Loop over all *.md file to check?
  - [ ] Could take a while, but is the better approach if you don't want spelling mistake
  - [ ] Check if Hugo has a solution
- [ ] Adjust settings for "Related content" (or "See Also"). I want to include newer posts as well
- [X] Improve the books section. Books are now separate posts, but only show title. I want to include writer, cover-image and "read now" link (which goes to https://read.amazon.com)
- [ ] Add a "Buy the book" link, to earn commission on Amazon
- [ ] Process images, pretty amazing what Hugo can do. See [docs about Image processing](https://gohugo.io/content-management/image-processing/)
- [ ] Include Author (writer) as a factor to generate related content
- [ ] On Hugo site, hovering over code examples widens them automatically. I want that too.
- [ ] On the page displaying a specific tag, for instance [/tags/reading/](), add links to all other tags
- [ ] writers on book pages are being lowercased
  - [ ] which file? >
- [ ] Add search

