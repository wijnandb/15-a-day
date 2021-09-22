--- 
draft: true
title: "Scotch whisky Sassenheim"
date: "2021-09-06T09:22:42+0200"
layout: post
tags: ["business", "platform", "notes","scotch","whisky"]
slug: "scotch-whisky-sassenheim"
---

Typo: [resigns (it now says "resignes")](https://scotchwhiskyinvestments.com/en/about-us/)

Different 'brandnames':
- scotchwhiskyinvestments
- scotchwhiskyexchange
- world whisky index
- 


## Domain names
Shorter, easier to remember domain name.
- whisky-index
- whsk (.nl, .eu available)
- wskx (.nl, .eu available)
- 



## Competition:
- [https://www.thewhiskyexchange.com/](https://www.thewhiskyexchange.com/)
- [Rare whisky](https://www.rarewhisky101.com/)
- [Whiskey Wealth Club](https://whiskeywealthclub.com/)
- [Master of Malt](https://www.masterofmalt.com/)
- [Whisky Invest Direct](https://www.whiskyinvestdirect.com/)
- 

## Scotch areas
- Highland
- Speyside
- Island
- Lowland
- Islay
- Campbeltown


## Whisky brands:
- Ardmore
- Ardnamurchan (non-peated)
- Ardnamurchan (peated)
- Auchentoshan
- Auchroisk
- Benrinnes
- Blair Athol
- Borders
- Bunnahabhain
- Cameronbridge
- Caol Ila
- Dailuaine
- Deanston
- Girvan
- Glenlossie
- Glen Elgin
- Glen Garioch
- Glen Moray
- Glen Spey
- Inchgower
- Invergordon
- Kirkcowan
- Kirkinner
- Ledaig
- Linkwood
- Mannochmore
- Nethermill
- North British
- Starlaw
- Strathenry
- Strathmill
- Teaninich
- Tobermory
- Tombae
- Tormore
- Tullibardine

## Scraping prices
- [Wine searcher](https://www.wine-searcher.com/most-expensive-whisky)
- [The whisky shop](https://www.whiskyshop.com/)
- [The whiskey exchange](https://www.thewhiskyexchange.com/)

## Ratings and reviews
- [Whisky base](https://www.whiskybase.com/)
- 


## Scraping the whisky exchange
Startpage (all Single Malt whiskies): https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky
Currently: 
- 2572 available whiskies, 
- 2812 including out of stock bottles.
- 74 limited editions
- Productpages: https://www.thewhiskyexchange.com/p/{x}/ x between 0 and 58996 (including other drinks than Scotch)
- Pages per region:
  - [Highland](https://www.thewhiskyexchange.com/c/313/)
  - [Speyside](https://www.thewhiskyexchange.com/c/314/)
  - [Island](https://www.thewhiskyexchange.com/c/315)
  - [Lowland](https://www.thewhiskyexchange.com/c/312/)
  - [Islay](https://www.thewhiskyexchange.com/c/50/)
  - [Campbeltown](https://www.thewhiskyexchange.com/c/316/)

On the region pages, a link can be found in:
- <strike>section class="js-filter-products"
- div class="product-list"
- ul class="product-list__list"</strike>
- li class="product-list__item"

Within the li, we are interested in:
- a href class product-row

We can either extract all information in teh overview, or follow the link and extract more information.
Following the link adds information like:
- bottler
- bottling date
- cask number
- age
- country
- colouring
- vintage
- region

Taking option 1 first:
- a href class="product-row"
- div class product-row__content
- h3 class="product-row__name"
- span class="product-row__name-secondary"
- p class="product-row__classification" (twice)
- p class="product-row__meta"
- p class="product-row__meta"
- p class="product-row__description"
- p class="product-row__image-container"
- p class="product-row__flag"
- p class="product-row__exclusive"
- p class="product-row__price"
- p class="product-row__unit-price"
- p class="product-row__message"

So how does the scraper work?
Startpoint per area:
https://www.thewhiskyexchange.com/c/50/?pg=1&psize=120&sort=lasc
https://www.thewhiskyexchange.com/c/312/?pg=1&psize=120&sort=lasc
https://www.thewhiskyexchange.com/c/313/?pg=1&psize=120&sort=lasc
https://www.thewhiskyexchange.com/c/314/?pg=1&psize=120&sort=lasc
https://www.thewhiskyexchange.com/c/315/?pg=1&psize=120&sort=lasc
https://www.thewhiskyexchange.com/c/316/?pg=1&psize=120&sort=lasc

- Loop through pages based on number of records found
  - in which field are the total results?
    - span class="js-paging-count__value--total"
  - alternative: check if value in span class="js-paging-count__value--end" > span class="js-paging-count__value--total"
- Scrape results

## Scraping the API

:authority: www.thewhiskyexchange.com
:method: POST
:path: /api/product/productlistdata
:scheme: https
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: nl,en-US;q=0.9,en;q=0.8,es;q=0.7
content-length: 905
content-type: application/json; charset=UTF-8
cookie: ASP.NET_SessionId=odazt0awk2iu2x2so0gmaqt3; __tweuid=cbf0dcc85b2f446eb226aefcdc3d5248; startedat=06/09/2021 08:48:32; rbuid=rbos-f5b6ff26-38c3-47c2-82d0-7bb161b8a1a7; __zlcmid=15wkJJcVB8C0jB0; ProductListPageVersion=v2; cookie=accepted; rtwe_viewmode=mode=list; rtwe_sorting=expr=lasc; rtwe_paging=pagesize=120; twe_recently_viewed_products=idlist=22277,21215,55615,11,56513,58995,58996,4000
dnt: 1
origin: https://www.thewhiskyexchange.com
referer: https://www.thewhiskyexchange.com/c/50/islay-single-malt-scotch-whisky?pg=2&psize=120&sort=lasc
sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
sec-ch-ua-mobile: ?1
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36
x-requested-with: XMLHttpRequest
