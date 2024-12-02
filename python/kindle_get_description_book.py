books =[["B000FBJCJE", "Snow Crash: A Novel", "fiction", "Stephenson, Neal:Stephenson, Neal:", "https://m.media-amazon.com/images/I/51yI5lXG7IL._SY600_.jpg", "https://read.amazon.com/?asin=B000FBJCJE", "http://s3.cn-north-1.amazonaws.com.cn/sitbweb-cn/content/B000FBJCJE/images/cover.jpg"],
["B000FC11A6", "Cryptonomicon", "fiction", "Stephenson, Neal:Stephenson, Neal:", "https://m.media-amazon.com/images/I/41E7EKgoryL._SY600_.jpg", "https://read.amazon.com/?asin=B000FC11A6", "http://s3.cn-north-1.amazonaws.com.cn/sitbweb-cn/content/B000FC11A6/images/cover.jpg"],
["B000FCKI7I", "Teacher Man: A Memoir (The Frank McCourt Memoirs)", "", "McCourt, Frank:McCourt, Frank:", "https://m.media-amazon.com/images/I/41eM4wMydvL._SY600_.jpg", "https://read.amazon.com/?asin=B000FCKI7I", "http://s3.cn-north-1.amazonaws.com.cn/sitbweb-cn/content/B000FCKI7I/images/cover.jpg"],
["B000FCKPHG", "Mindset: The New Psychology of Success", "", "Dweck, Carol S.:Dweck, Carol S.:", "https://m.media-amazon.com/images/I/41vS70Qo3rL._SY600_.jpg", "https://read.amazon.com/?asin=B000FCKPHG", "http://s3.cn-north-1.amazonaws.com.cn/sitbweb-cn/content/B000FCKPHG/images/cover.jpg"]
]

# scrape the content of a book from Amazon
# Links: for book in books:
#           storelink = "https://www.amazon.com/dp/" + book[0]

# follow the link and go for div id="iframeContent"
# get all the contents, as html, so including <b> and <br>

#from lxml import html
from bs4 import BeautifulSoup
import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

for book in books:
    link = "https://www.amazon.com/dp/" + book[0]
    page = requests.get(link, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify)
    #description = soup.find('div', id='iframeContent')
    description = soup.find("div", {"id": "iframeContent"})
    #print(''.join(map(str, description.contents)))
    print(description)
