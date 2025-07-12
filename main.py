import requests
from bs4 import BeautifulSoup

# --- Data Section ---
project_name = "Kali Academic Search"
# Let's use a more complex page with lots of text
wiki_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"


# --- Function Definitions ---
def display_startup_info():
    """This function prints the project's name."""
    print("Project Name:", project_name)
    print("---")

def scrape_page_content(url):
    """
    Connects to a URL, parses the HTML, and extracts all paragraph text.
    """
    print(f"Scraping content from {url}...")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Check for request errors

        soup = BeautifulSoup(response.text, 'lxml')

        # Find all <p> (paragraph) tags on the page
        paragraphs = soup.find_all('p')

        print(f"Found {len(paragraphs)} paragraph tags.")
        print("---")

        # Loop through each paragraph tag and print its clean text
        for p in paragraphs:
            print(p.get_text().strip()) # .strip() removes leading/trailing whitespace

    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")
    print("---")


# --- Main Execution ---
display_startup_info()
scrape_page_content(wiki_url)
print("Scraping complete.")