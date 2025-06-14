import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def discover_resources(url):
    """
    Discovers all links and forms on a given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return [], []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links
    links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag.get('href')
        # Join relative URLs with the base URL
        full_url = urljoin(url, href)
        links.add(full_url)

    # Find all forms
    forms = soup.find_all('form')

    print(f"Discovered {len(links)} links and {len(forms)} forms on {url}")
    return list(links), forms