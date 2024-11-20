--- 
draft: true
title: "Testing new version of Hugo"
date: "2021-12-14T10:03:52+0100"
layout: post
tags: ["hugo"]
slug: "testing-new-version-of-hugo"
---

I have just installed a new version of Hugo, version 0.90.1.

Struggled a bit, because I didn't fully understand what I was doing. I downloaded the latest version from https://github.com/gohugoio/hugo/releases (taking the linux64bit.tar.gz).

Unzipped it in the Downloads folder and then moved it to the /usr/local/ folder.

Moving the file required sudo, because I can't acccess /usr/local/ without sudo, so it had to be:
```bash
$ sudo mv ~/Downloads/hugo /usr/local/
```
Checking if it worked by looking up the version:
```bash
$ hugo version

```
The reason I needed a new version of Hugo was because I had trouble making it work on S3.
