import os
import subprocess

# Correct path to the SecretFinder script
SECRET_FINDER_PATH = "/home/asshu/tools/secretfinder/SecretFinder.py"

# Check if the SecretFinder script exists
if not os.path.isfile(SECRET_FINDER_PATH):
    print(f"SecretFinder script not found at {SECRET_FINDER_PATH}")
    exit(1)

# Prompt the user to enter the path to the URL file
URL_FILE = input("Please enter the path to the URL file: ")

# Check if the URL file exists
if not os.path.isfile(URL_FILE):
    print(f"URL file not found at {URL_FILE}")
    exit(1)

# Read the URL file and run SecretFinder for each URL
with open(URL_FILE, 'r') as file:
    for url in file:
        url = url.strip()
        if url:  # Check if the URL is not empty
            print(f"Scanning URL: {url}")
            try:
                subprocess.run(
                    ["python3", SECRET_FINDER_PATH, "-i", url, "-o", "cli"],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error scanning URL {url}: {e}")