# --- Data Section ---
project_name = "Kali Academic Search"
academic_engines = ["Google Scholar", "arXiv.org", "JSTOR", "PubMed Central"]

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

# --- Main Execution ---
# Where the program starts running
display_startup_info()
list_target_engines()
print("Initalization complete.")

