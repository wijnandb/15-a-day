---
title: 'Hugo: better suited static site generator?'
date: "2021-09-01 09:21:24"
layout: post
tags: ["hugo", "static site generator", "tags"]
draft: false
---

There are several static site generators that I have tried, and [Hugo] is now up for review.

It claimms to be the fastest, with pagebuilds of 1 ms per page. That is certainly impressive, but there are other aspects of Hugo that appeal to me.

I have looked at [Jekyll] and [Pelican]. I like Jekyll because it is tightly integrated with Github pages, making it easy to launch a site. What I don't like about Jekyl is that it is written in Ruby, mainly because I don't know Ruby well enough.

For that reason, I have also looked at [Pelican] because it is written in [Python], which is a language I know and like. Even though you'd think it is an advantage to use a site generator in a language you know, the truth is that I never get to the point that I really need or want to look at the underlying code: if the static site generator does what it is supposed to do, I already spend enough time on writing content and trying to make it look good.

That made me circle back to Jekyll: easy to launch a site on Github pages, what more do you need?

Well, there are some things left to desire if you look at Jekyll. And that brought me to [Hugo].

First of all, the community around it seems very active, it has 53.9K stars on Github. It also seems to be aiming at providing a solid solution for building a static site, and not just a blog (like Jekyll seems to be doing). It's written in [Go] and is supposedly blazingly fast.

Whatever, I am trying to justify that I am looking into Hugo, let's just have a go and tell you what I'm coming across.

- install
- restart shell so hugo command can be found
- create new hugo site: hugo new site name_of_new_site
- git init
- git add .
- add a theme: 
  ``` bash 
  $ git submodule add https://github.com/luizdepra/hugo-coder.git themes/hugo-coder 
  ```
- fill out _config.toml
- Build and launch site: 
  ``` 
  $ hugo server -D 
  ```
  
  {{< notice info >}}
    You are reading this, so it works!
    Site been build and deployed.
    Very enthusiastic about Hugo, it is blazing fast
  {{< /notice >}}

Getting the site fully working on AWS S3 was not completely trouble free, main problem turned out to be the fact that S3 isn't a webserver, so you can't tell it to look for index.html if it gets to a directory. Hugo has a solution for this, called uglyURLs, so setting that to true fixed the issue partially. New problem I then encountered was the very good caching that Cloudfront uses: the changes to uglyURLs was in effect, but I was still seeing the old (wrong) URLs, which gave errors.

Luckily there is a way of clearing the cache, which is called *Invalidation* on Cloudfront. Not a vbery intuitive name, I would say, but once you know that, you ca make it work.

[Hugo]: https://gohugo.io/
[Go]: https://golang.org/
[Jekyll]:
[Pelican]: 
