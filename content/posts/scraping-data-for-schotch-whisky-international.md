--- 
draft: true
title: "Scraping data for Schotch Whisky International"
date: "2021-09-24T13:52:28+0200"
layout: post
tags: ["whisky","scotch","scraping"]
slug: "scraping-data-for-schotch-whisky-international"
---

Because I tend to be all over the place, I need to find a good method of scraping al the data of the different sites.

By splitting up the different tasks in functions, it might be easier for me to do a little work everytime and making progress. I think starting with the last piece, the scraping on the productpage, I can make the fastest progress. I can send a (or some) examples of scraped items to Niels, who can then comment on them, so I can make adjustments. Splitting up the 'soup creation' (or the selenium task) from the scraping, makes the code less redundant and better to read/maintain.

I have started out creating different files for different sites, but since there are quite some functions that are needed in every scrape, I'm thinking about putting it together in one scraping file.


