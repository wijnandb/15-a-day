import random
import requests
import os

# Get the latest XKCD comic number
latest_comic_url = "https://xkcd.com/info.0.json"
response = requests.get(latest_comic_url)
latest_comic = response.json()["num"]

# Pick a random comic
random_comic_number = random.randint(1, latest_comic)
random_comic_url = f"https://xkcd.com/{random_comic_number}/info.0.json"
comic_response = requests.get(random_comic_url)
comic_data = comic_response.json()

# Prepare content for Hugo
content = f"""
---
title: "Random XKCD Comic"
date: {comic_data['year']}-{comic_data['month']:0>2}-{comic_data['day']:0>2}
comic_title: "{comic_data['title']}"
comic_img: "{comic_data['img']}"
comic_alt: "{comic_data['alt']}"
---
"""

# Save to Hugo content
content_path = "content/random_xkcd.md"
with open(content_path, "w") as file:
    file.write(content)
