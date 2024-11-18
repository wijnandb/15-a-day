---
draft: false
title: Show books collection dynamic with Javascript
date: "2024-11-15T09:05:43+0200"
layout: post
tags: ["website", "javascript"]
slug: "show-books-collection-dynamic-with-javascript"
---

On this website, I have a bookcollection. All the books I have on my Kindle, are displayed here. Showing the cover, a summary, key takeaways. In addition to that, I have added *tags* to each book, so I can filter the collection and only show the books with that specific *tag*.

However, these pages with books per tag are a lot more boring than the general collection of books, where we are showing all the covers.
So, showing the books with covers on the filtered pages would be nice. But, when thinking about that, it seems that having the content for the book-information in a csv or a JSON is a lot more practical: easier to maintain and update, faster to display and filter.

Instead of building a new Hugo site when adding a book, we simply add a book to the JSOn and it will be displayed whenever the page is visited.

OK, that sounds easy and it might not be too complicated, but it still is some work that needs to be done.

Let's start asking Chad, our programming wizard, how to approach this. 
In order for them to help us, let's describe the problem:

"In a Hugo site, we have a collection of books. We display the covers of these books on a list page. All works fine, but we would also like to display the covers when we filter the books by tag. Now I understand that it's possible to do that inside Hugo, but I'd rather approach it differently: I want to store the book information in a CSV or a JSON file, and use Javascript to display the book information. That means: 
- displaying all books, with pagination
- order the books on date, title, author name
- filter the books by tag

This will essentially be one page, however I'd like to make sure each different view has its own URL. So that means we want the Javascript to update the URL and we want the Javascript to read the information used to filter, sort and display the book(s) from the URL.

Before going to the creation of the necessary code, let's address some potential issues:
- can we combine such a page with a Hugo site?
- how will we construct our URL's?

This didn't immediately give me the setup I wanted, so I explained how I wanted the URLs to be constructed:

Is it possible to have a URL /books/ which displays all the books.
Then the url /books/#/book/book1/ displays the information about book1.
/books/#/tag/tag1/ displays all the books with tag1.
/books/#/author/author1/ displays all the books from author1.

So the Javascript both reads and updates the URL and 'knows' which information to extract from the JSON, based on the URL.

I also checked (again) if and how this would play together with Hugo, and this was the answer:


Create the Layout
In the layouts folder, add a new layout for the books page:

File: layouts/books.html
Content:
```HTML
{{ partial "header.html" . }}
<div id="app"></div>
<script src="/js/routing.js"></script>
{{ partial "footer.html" . }}

```
This layout includes the #app container for JavaScript rendering.

Full conversation on https://chatgpt.com/share/673707fd-b898-800a-9f27-4eb038060331 

Now in lightof my procrastination/ADD/ADHD/being easily distracted issues: I now have the solution laid out in front of me.
The only thing I need to do, is build the damn thing.

Just follow the steps and I have what I want.

But instead of doing that, I realise that I lose interest, I don't feel like doing it.
What does that mean?
What can I learn from that?

I think it's not such a big problem. It's monday, I have taken some detours (installing Calibre, not really getting what I wanted) and deciding that being able to generate/update the CSV or JSON that will fuel my site is more important to tackle first (not really agreeing with myself on that one, but I have tackled it, so that's good).

Here's the solution to get the contents of my Kindle collection:

https://chatgpt.com/share/673b110a-aa34-800a-9455-b4b3287698f0

The solution is a little Javascript that you run in the console of your browser and which will get you a CSV with the information of all your Kindle books.

```Javascript
// Initialize variables
let xhr = new XMLHttpRequest();
let domain = 'https://read.amazon.com/';
let items = [];
let csvData = "";

// Function to retrieve items list
function getItemsList(paginationToken = null) {
    let url = domain + 'kindle-library/search?query=&libraryType=BOOKS' +
        (paginationToken ? '&paginationToken=' + paginationToken : '') +
        '&sortType=recency&querySize=50';
    xhr.open('GET', url, false);
    xhr.send();
    if (xhr.status === 200) {
        let data = JSON.parse(xhr.responseText);
        if (data.itemsList) {
            items.push(...data.itemsList);
        }
        if (data.paginationToken) {
            getItemsList(data.paginationToken);
        }
    } else {
        console.log('Failed to retrieve data');
    }
}

// Start the retrieval process
getItemsList();

// Format data as CSV
items.forEach(item => {
    let authors = item.authors ? item.authors.join('; ') : '';
    csvData += `"${item.asin}","${item.title}","${authors}","${item.webReaderUrl}","${item.productUrl}","${item.resourceType}"\n`;
});

// Create a Blob from the CSV data
const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
const url = URL.createObjectURL(blob);

// Create a temporary link to trigger the download
const link = document.createElement('a');
link.href = url;
link.setAttribute('download', 'kindle_books.csv');
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
```

ChatGPT suggested getting a JSON version of the list of books and I asked if therewere more fields to include, which there were, resulting in the following script to create the JSON:

```Javascript
// Initialize variables
let xhr = new XMLHttpRequest();
let domain = 'https://read.amazon.com/';
let items = [];

// Function to retrieve items list
function getItemsList(paginationToken = null) {
    let url = domain + 'kindle-library/search?query=&libraryType=BOOKS' +
        (paginationToken ? '&paginationToken=' + paginationToken : '') +
        '&sortType=recency&querySize=50';
    xhr.open('GET', url, false);
    xhr.send();
    if (xhr.status === 200) {
        let data = JSON.parse(xhr.responseText);
        if (data.itemsList) {
            items.push(...data.itemsList);
        }
        if (data.paginationToken) {
            getItemsList(data.paginationToken);
        }
    } else {
        console.log('Failed to retrieve data');
    }
}

// Start the retrieval process
getItemsList();

// Format data as JSON
const jsonData = JSON.stringify(items, null, 2);

// Create a Blob from the JSON data
const blob = new Blob([jsonData], { type: 'application/json;charset=utf-8;' });
const url = URL.createObjectURL(blob);

// Create a temporary link to trigger the download
const link = document.createElement('a');
link.href = url;
link.setAttribute('download', 'kindle_books.json');
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
```

