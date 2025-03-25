import os
import requests
import json
import yaml
import slugify

# Define paths
JSON_FILE = "content/books.json"  # Replace with your JSON file path
MARKDOWN_DIR = "content/books"  # Replace with your markdown files directory
COVERS_DIR = "static/images/bookcovers/small"  # Replace with your cover images directory
IMAGE_LINK_DIR = "images/bookcovers/small"  # Replace with your cover images directory

# Fetch additional data from Google Books
def fetch_google_books_data(title, authors):
    API_URL = "https://www.googleapis.com/books/v1/volumes"
    
    # Normalize authors and use the first author for the query
    normalized_authors = normalize_authors(authors)
    first_author = normalized_authors[0] if normalized_authors else ""
    
    # Clean and reformat the first author's name
    first_author_cleaned = format_author_name(first_author)
    
    # Construct the query
    query = f"intitle:{title} inauthor:{first_author_cleaned}"
    params = {"q": query}
    
    # API request
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            return data["items"][0]["volumeInfo"]  # Return the first match
    return {}

# Generate a slug for the title
def generate_slug(title):
    return slugify.slugify(title)

# Check if a markdown file already exists
def markdown_exists(title):
    slug = generate_slug(title)
    return any(slug in filename for filename in os.listdir(MARKDOWN_DIR))

# Download the cover image from productUrl
def download_cover_image(book_data):
    # Get the product URL and ASIN from the book data
    url = book_data.get("productUrl")
    asin = book_data.get("asin")
    
    # If the URL or ASIN is missing, return None
    if not url or not asin:
        print(f"Missing productUrl or ASIN for book: {book_data.get('title', 'Unknown Title')}")
        return None

    # Path to store the image
    cover_path = os.path.join(COVERS_DIR, f"{asin}.jpg")
    
    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Write the image to a file
            with open(cover_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Cover downloaded for ASIN {asin} at {cover_path}")
            return cover_path  # Return the local path to the cover
        else:
            print(f"Failed to download cover for ASIN {asin}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error downloading cover for ASIN {asin}: {e}")
    
    return None  # Return None if download fails


def format_author_name(name):
    parts = name.split(", ")
    if len(parts) == 2:
        return f"{parts[1].title()} {parts[0].title()}"
    return name.title()  # For names without a comma

def normalize_authors(authors):
    if len(authors) == 1 and ":" in authors[0]:  # Check for single string with colons
        # Split by colon and clean up extra spaces or colons
        return [author.strip().strip(":") for author in authors[0].split(":")]
    return authors  # Return as is if already a clean list

# Create a markdown file
def create_markdown(book_data, metadata, cover_path):
    slug = generate_slug(book_data["title"])
    authors = normalize_authors(book_data["authors"])  # Normalize authors here
    frontmatter = {
        "layout": "book",
        "title": book_data["title"],
        "authors": authors,  # Use the normalized authors
        "date": metadata.get("publishedDate", "2000-01-01"),
        "cover": cover_path,
        "tags": metadata.get("categories", []),
        "categories": ["book"],
        "largecover": metadata.get("imageLinks", {}).get("medium", ""),
        "readlink": book_data.get("webReaderUrl", ""),
        "ASIN": book_data["asin"],
        "affiliatelink": f"https://www.amazon.com/dp/{book_data['asin']}?tag=prcptm-20",
    }

    markdown_content = f"---\n{yaml.dump(frontmatter)}---\n"
    markdown_content += f"# {book_data['title']}\n\n## Summary\n"
    markdown_content += metadata.get("description", "Summary not available.") + "\n\n"
    # markdown_content += "## Key Takeaways\n1. To be filled in later.\n"

    filename = os.path.join(MARKDOWN_DIR, f"{slug}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

# Main process
def process_books():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        books = json.load(f)

    for book in books:
        if not markdown_exists(book["title"]):
            metadata = fetch_google_books_data(book["title"], ", ".join(book["authors"]))
            cover_url = metadata.get("imageLinks", {}).get("thumbnail", "")
            cover_path = download_cover_image(book)
            create_markdown(book, metadata, cover_path)
            print(f"Markdown and cover created for: {book['title']}")

if __name__ == "__main__":
    os.makedirs(MARKDOWN_DIR, exist_ok=True)
    os.makedirs(COVERS_DIR, exist_ok=True)
    process_books()
