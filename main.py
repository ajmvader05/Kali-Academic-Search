import requests
from bs4 import BeautifulSoup

# --- Function Definitions ---
def get_user_query():
    """Prompts the user for a search topic and returns it."""
    print("Please enter a topic to search on Wikipedia:")
    query = input("> ") # Display a ">" prompt and wait for user input
    return query

def construct_url(query):
    """Takes a user query and constructs a valid Wikipedia URL."""
    # Replace spaces with underscores for the URL
    formatted_query = query.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{formatted_query}"
    return url

def scrape_page_content(url):
    """
    Connects to a URL, parses the HTML, and extracts all paragraph text.
    """
    print(f"\nScraping content from {url}...")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')
        
        # Check if it's a "page does not exist" page
        if "Wikipedia does not have an article with this exact name." in response.text:
            print("---")
            print("This Wikipedia page does not exist.")
            print("Please check your spelling or try a different query.")
            return # Exit the function early

        paragraphs = soup.find_all('p')
        print(f"Found {len(paragraphs)} paragraph tags.")
        print("---")

        for p in paragraphs:
            print(p.get_text().strip())

    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")
    print("---")


# --- Main Execution ---
user_topic = get_user_query()

if user_topic: # Only proceed if the user actually typed something
    search_url = construct_url(user_topic)
    scrape_page_content(search_url)
    print("Scraping complete.")
else:
    print("No query entered. Exiting.")