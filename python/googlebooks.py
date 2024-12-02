import requests

def fetch_google_books_data(title, author):
    API_URL = "https://www.googleapis.com/books/v1/volumes"
    query = f"intitle:{title} inauthor:{author}"
    params = {"q": query}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            return data["items"][0]["volumeInfo"]  # Return the first match
    return None

book_data = fetch_google_books_data("Measure What Matters", "John Doerr")
# print(book_data)


def fetch_open_library_data(isbn):
    API_URL = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        key = f"ISBN:{isbn}"
        return data.get(key, {})
    return None

print(fetch_open_library_data("052553623X"))

