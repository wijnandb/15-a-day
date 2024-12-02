import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def search_words_in_urls(start_urls, search_words, max_depth=2):
    """
    Recursively searches for specific words in the content of URLs starting from given URLs.

    Args:
        start_urls (list): List of starting URLs to crawl.
        search_words (list): List of words or phrases to search for.
        max_depth (int): Maximum depth for recursive crawling.

    Returns:
        dict: A dictionary where keys are URLs and values are lists of found words.
    """
    visited = set()
    results = {}

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        
        print(f"Fetching URL: {url}")
        visited.add(url)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()

            # Search for words
            found_words = [word for word in search_words if word.lower() in text]
            if found_words:
                results[url] = found_words

            # Find and crawl links recursively
            for link in soup.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                if next_url.startswith("http") and next_url not in visited:
                    crawl(next_url, depth + 1)

        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    for start_url in start_urls:
        crawl(start_url, depth=0)

    return results

# Example usage
if __name__ == "__main__":
    # List of starting URLs to search
    start_urls = [
        'https://www.lucasonderwijs.nl',
'https://www.spoutrecht.nl',
'https://www.dehaagsescholen.nl',
'https://www.rvko.nl',
'https://www.pcou.nl',
'https://www.ksu-utrecht.nl',
'https://www.stichtingboor.nl',
'https://www.zonova.nl',
'https://www.twijs.nl',
'https://www.stwt.nl',
'https://www.spaarnesant.nl',
'https://www.amosonderwijs.nl',
'https://www.awbr.nl',
'https://www.elamal.nl',
'https://www.alamana.nl',
'https://www.unicoz.nl',
'https://www.askoscholen.nl',
'https://www.innoord.nl',
'https://www.floresonderwijs.nl',
'https://www.pit-ko.nl',
'https://www.ooz.nl',
'https://www.kindante.nl',
'https://www.symbiohengelo.nl',
'https://www.staij.nl',
'https://www.sooog.nl',
'https://www.mosalira.nl',
'https://www.bsyunusemre.nl',
'https://www.signumonderwijs.nl',
'https://www.akkoord-po.nl',
'https://www.asg.nl',
'https://www.skpo.nl',
'https://www.conexus.nu',
'https://www.salto-eindhoven.nl',
    ]

    # Words or phrases to search for
    search_words = ["brede school", "rijke schooldag", "school en omgeving", "subsidie"]

    # Maximum crawling depth
    max_depth = 2

    # Search and print results
    results = search_words_in_urls(start_urls, search_words, max_depth=max_depth)
    for url, found_words in results.items():
        print(f"\nURL: {url}")
        if found_words:
            print(f"Found words: {', '.join(found_words)}")
        else:
            print("No words found.")

        
