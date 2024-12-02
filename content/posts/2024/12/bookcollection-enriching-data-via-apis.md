--- 
draft: true
title: "Bookcollection. Enriching data via APIs"
date: "2024-12-02T10:37:52+0100"
layout: post
tags: ["webdevelopment","books","API"]
slug: "bookcollection-enriching-data-via-apis"
---

I have a collection of books that I showcase on my website. 
I want to add new books.
What does it take to do that?
- download the complete collection from Amazon, https://read.kindle.com 
- visit the books to download the cover and store it locally
- create markdown files for the books that don't exist on the site yet
- add information to the markdown files, e.g. from Google Books API 
- maybe the actions are not in the right order yet

What I am getting from Amazon is the asin, title of book, authors, link to read the book and the url of the cover image.

What I'd like to add is:
- publication year
- synopsis 
