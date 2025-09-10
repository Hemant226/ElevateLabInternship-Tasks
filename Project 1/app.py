from flask import Flask, render_template, request
from crawler import discover_resources
from scanner import scan_sql_injection, scan_xss

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_url = request.form['url']
    if not target_url.startswith('http'):
        target_url = 'http://' + target_url

    print(f"Starting scan on {target_url}")

    # 1. Crawl the website to find links and forms
    links, forms = discover_resources(target_url)

    # --- Store findings ---
    # According to the guidelines, we need to log each vulnerability.
    # For a web UI, a list of strings is a simple way to start.
    vulnerabilities_found = []

    # 2. Scan for XSS on discovered links
    print("\n--- Scanning for XSS ---")
    for link in links:
        if scan_xss(link):
            vulnerabilities_found.append(f"Reflected XSS found at: {link}")

    # 3. Scan for SQL Injection in discovered forms
    print("\n--- Scanning for SQL Injection ---")
    for form in forms:
        if scan_sql_injection(target_url, form):
             action = form.get('action', 'N/A')
             vulnerabilities_found.append(f"SQL Injection possibility in form with action: {action}")

    return render_template('results.html', url=target_url, vulnerabilities=vulnerabilities_found)

if __name__ == '__main__':
    # Use debug=False in a production environment
    app.run(debug=True)