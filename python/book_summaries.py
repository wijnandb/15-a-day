import os
from openai import OpenAI
from pathlib import Path
import re
import shutil
from dotenv import load_dotenv

load_dotenv()

# Directory containing markdown files
unprocessed_dir = Path("/home/wijnandb/sites/15-a-day/content/books/add_summary")
processed_dir = Path("/home/wijnandb/sites/15-a-day/content/books")
limit = 10


def extract_metadata(markdown_content):
    """Extract metadata from markdown content."""
    metadata = {}
    lines = markdown_content.splitlines()
    in_front_matter = False
    
    for line in lines:
        if line.strip() == "---":
            in_front_matter = not in_front_matter
        elif in_front_matter:
            match = re.match(r"(\w+): (.+)", line)
            if match:
                key, value = match.groups()
                metadata[key] = value.strip().strip('"')
    
    return metadata



def verify_and_generate_summary(book_title, authors):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (f"Please provide an overview of the book titled {book_title} written by {authors}. If you're unsure about any specific details, please omit them rather than speculate. This response should only include factual information based on verified knowledge."
                " Please include: "
                "Summary: A concise summary that covers the main themes, key plot points, or concepts."
                "Review: A short review that assesses the book’s impact, strengths, and any notable weaknesses or critiques."
                "Key Takeaways: List several actionable insights, lessons, or memorable ideas presented in the book."
                "Recommendation: A brief recommendation that suggests who might benefit from reading the book and why."
                "Create the text in markdown format.")
            }
        ],
        model="gpt-4o",
    )


    
    # Extract the response text
    # generated_text = chat_completion['choices'][0]['message']['content']
    print(chat_completion)
    generated_text = chat_completion.choices[0].message.content
    # print(generated_text)
    
    # Check if the book is recognized by the AI
    if "I don't know this book" in generated_text.lower():
        return None
    return generated_text


def process_markdown_files(directory, processed_directory, limit=None):
    processed_count = 0

    for markdown_file in directory.glob("*.md"):
        if limit and processed_count >= limit:
            break
        
        # Read the markdown file
        with open(markdown_file, 'r') as file:
            content = file.read()
        
        # Extract metadata
        metadata = extract_metadata(content)
        book_title = metadata.get("title")
        authors = metadata.get("authors")
        
        # Check if the book is recognized and generate summary/takeaways if so
        generated_text = verify_and_generate_summary(book_title, authors)
        
        if generated_text:
            # Replace "The book" or any existing content after front matter with the summary
            new_content = re.sub(r"(---\n.*?---\n)(.*?)(\n|$)", rf"\1{generated_text}\3", content, flags=re.DOTALL)
            
            # Write the updated content back to the markdown file
            with open(markdown_file, 'w') as file:
                file.write(new_content)
            
            print(f"Processed {markdown_file.name}")
            processed_count += 1
            
            # Move the file to the processed directory
            shutil.move(markdown_file, processed_directory / markdown_file.name)
        else:
            print(f"Book '{book_title}' by {authors} is not recognized by the AI.")




def clean_empty_content_files(directory):
    """Remove content from files that only contain 'The book' and whitespace."""
    for markdown_file in directory.glob("*.md"):
        # Read the markdown file
        with open(markdown_file, 'r') as file:
            content = file.read()
        
        # Check if the content only has "The book" and whitespace after the front matter
        if re.search(r"(---\n.*?---\n)(\s*The book\s*)$", content, flags=re.DOTALL):
            # Remove everything after the front matter
            cleaned_content = re.sub(r"(---\n.*?---\n)(\s*The book\s*)$", r"\1", content, flags=re.DOTALL)
            
            # Write the cleaned content back to the markdown file
            with open(markdown_file, 'w') as file:
                file.write(cleaned_content)
            
            print(f"Cleaned content in {markdown_file.name}")
        else:
            print(f"No cleaning needed for {markdown_file.name}")


def ensure_categories_in_front_matter(directory, limit=None):
    """Ensures 'categories: ['book']' exists in the front matter if it's missing."""
    processed_count = 0

    for markdown_file in directory.glob("*.md"):
        if limit and processed_count >= limit:
            break

        # Read the markdown file
        with open(markdown_file, 'r') as file:
            content = file.read()

        # Check if "categories:" exists in the front matter
        if "categories:" not in content:
            # Insert categories: ['book'] before the closing front matter marker (---)
            content = re.sub(r"(---\n.*?)(---)", r"\1categories: ['book']\n\2", content, flags=re.DOTALL)

            # Write the updated content back to the markdown file
            with open(markdown_file, 'w') as file:
                file.write(content)
            
            print(f"Added categories to {markdown_file.name}")
            processed_count += 1
        else:
            print(f"Categories already present in {markdown_file.name}")


# clean_empty_content_files(unprocessed_dir)
# ensure_categories_in_front_matter(unprocessed_dir)
process_markdown_files(unprocessed_dir, processed_dir)
