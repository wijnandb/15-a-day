import requests

def fetch_metadata_from_openlibrary(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
    response = requests.get(url)
    return response.json()

# Example: Fetch metadata for a specific ISBN
isbn = "9781449355739"  # Replace with your book's ISBN
metadata = fetch_metadata_from_openlibrary(isbn)
print(metadata)
