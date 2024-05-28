# API Key Finder using SecretFinder

This Python script automates the process of scanning URLs for secrets, such as API keys, using the `SecretFinder` tool. It prompts the user for a file containing a list of URLs and then processes each URL using `SecretFinder`.

## Prerequisites

- Python 3.x
- SecretFinder tool

## Installation

1. **Clone the SecretFinder Repository**:
    ```bash
    git clone https://github.com/m4ll0k/SecretFinder.git
    ```

2. **Navigate to the SecretFinder Directory**:
    ```bash
    cd SecretFinder
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Python Script**:
    Save the `apifinder.py` script to a convenient location. Make sure to update the `SECRET_FINDER_PATH` variable in the script to the correct path to `secretfinder.py`.

## Usage

1. **Prepare Your URLs File**:
    Create a file named `urls.txt` (or any name you prefer) that contains the list of URLs you want to scan, one per line.

2. **Run the Script**:
    Execute the Python script and provide the path to your URL file when prompted.
    ```bash
    python3 apifinder.py
    ```

3. **Enter the Path to the URL File**:
    When prompted, enter the path to your `urls.txt` file.

## Example


### Running the Script
```bash
$ python3 apifinder.py
Please enter the path to the URL file: /path/to/urls.txt
Scanning URL: http://example.com
...
Scanning URL: http://testsite.com
...
Scanning URL: http://mysite.com
...
