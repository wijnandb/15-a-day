import requests
from bs4 import BeautifulSoup

def fetch_metadata_from_amazon(asin):
    url = f"https://www.amazon.com/dp/{asin}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract metadata
    metadata = {}
    try:
        metadata["publication_date"] = soup.find("span", string="Publication date").find_next("span").text
        metadata["publisher"] = soup.find("span", string="Publisher").find_next("span").text
    except AttributeError:
        pass  # Metadata not found
    
    return metadata

# Example: Fetch metadata for a specific ASIN
asin = "B000FA64PK"
metadata = fetch_metadata_from_amazon(asin)
print(metadata)
