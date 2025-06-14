# Web Application Vulnerability Scanner

A simple but effective web application vulnerability scanner built with Python and Flask. This tool is designed to crawl a given web application, identify input vectors, and test for common security vulnerabilities such as Cross-Site Scripting (XSS) and SQL Injection (SQLi).

This project was developed as part of the Elevate Labs Internship Program. 

## 🚀 Key Features

-   **Automated Crawling**: Automatically discovers all reachable links and forms on the target website. 
-   **SQL Injection (SQLi) Detection**: Tests forms for basic error-based SQL Injection vulnerabilities.
-   **Cross-Site Scripting (XSS) Detection**: Injects payloads into URLs and forms to detect reflected XSS vulnerabilities.
-   **User-Friendly Web Interface**: A clean and simple UI built with Flask that allows users to easily start scans and view the results.
-   **Clear Reporting**: Presents a list of all potential vulnerabilities found during the scan session.

## 🛠️ Tools & Technologies

-   **Backend**: Python
-   **Web Framework**: Flask 
-   **HTTP Requests**: `requests` library 
-   **HTML Parsing**: `BeautifulSoup4` 
-   **Frontend**: Basic HTML

## ⚙️ Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3 and `pip` installed on your system.

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd your-repository-name
    ```

3.  **Create and activate a virtual environment (Recommended):**
    -   **Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    -   **macOS / Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask server:**
    ```sh
    python app.py
    ```

2.  **Open your web browser** and navigate to:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

## 📝 How to Use

1.  Once the application is running, you will see a simple input field.
2.  Enter the full URL of the web application you want to test (e.g., `http://example.com`).
3.  Click the **"Start Scan"** button.
4.  The scanner will crawl the site and perform its tests. The results will be displayed on a new page, listing any potential vulnerabilities that were found.

## ⚠️ Ethical Disclaimer

This tool is intended for educational purposes and for testing web applications that you **own or have explicit, written permission to test**. Unauthorized scanning or testing of websites is illegal and unethical. The creator of this tool is not responsible for any misuse or damage caused by this program. Always act responsibly.

## 🔮 Future Improvements

While this tool is functional, there's always room to grow! Here are some potential future enhancements:

-   [ ] Implement tests for more vulnerabilities from the OWASP Top 10, such as CSRF and Command Injection.
-   [ ] Add severity levels (e.g., Low, Medium, High) to the vulnerability reports. 
-   [ ] Enhance the crawler to handle sites that heavily rely on JavaScript.
-   [ ] Allow scan results to be exported to a PDF or CSV file.
-   [ ] Implement a database to store scan history and track vulnerability remediation over time.

---
