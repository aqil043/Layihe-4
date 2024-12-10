import requests

def get_wikipedia_content(page_title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": page_title,
        "exintro": True,  # Get only the introductory section
        "explaintext": True  # Get plain text instead of HTML
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract page content from the response
    page_id = next(iter(data["query"]["pages"]))
    content = data["query"]["pages"][page_id]["extract"]

    return content

# Fetch content of NASA Wikipedia page
nasa_content = get_wikipedia_content("NASA")
print(nasa_content)