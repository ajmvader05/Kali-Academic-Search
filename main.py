import requests #Import the library we installed with pip
# --- Data Section ---
project_name = "Kali Academic Search"
academic_engines = ["Google Scholar", "arXiv.org", "JSTOR", "PubMed Central"]
test_url = "https://example.com"

# --- Function Definitions ---
def display_startup_info():
	"""Docstring - explains what a function does."""
	print("Project Name:", project_name)
	print("---")

def list_target_engines():
	"""Prints all engines in the academic_engines list."""
	print("Target Academic Engines:")
	for engine in academic_engines:
		print("-", engine)
	print ("---")
def ping_test_site(url):
	"""
	Connects to a URL and prints the status - core of a web request
	"""
	print(f"Pinging {url}...")
	try:
		response = requests.get(url, timeout=5)
		print(f"Status Code: {response.status_code}")
		if response.status_code == 200:
			print("Connection sucessful.")
	except requests.exceptions.RequestException as e:
		print (f"Connection failed {e}")
	print("---")

# --- Main Execution ---
# Where the program starts running
display_startup_info()
list_target_engines()
ping_test_site(test_url)
print("Initalization complete.")

