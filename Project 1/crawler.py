import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def discover_resources(url):
    """
    Discovers all links and forms on a given URL.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; YourScanner/1.0)'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return [], []

    if not response.content:
        print(f"No content received from {url}")
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
    forms = []
    for form in soup.find_all('form'):
        action = form.get('action', '')
        method = form.get('method', 'get').lower()
        full_action = urljoin(url, action)
        forms.append({'method': method, 'action': full_action})

    print(f"Discovered {len(links)} links and {len(forms)} forms on {url}")
    return list(links), forms