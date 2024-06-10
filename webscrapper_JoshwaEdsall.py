"""
Champlain College Current Students Web Scraper

This script fetches the HTML content from the Champlain College current students page
and extracts information such as 'Information For' links and login form fields.

Thammuz95


"""

import urllib.request
from bs4 import BeautifulSoup


# Function to fetch HTML content from a URL
def fetch_html(url):
    """
    Fetches HTML content from the specified URL.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        bytes: The HTML content as bytes.
    """
    print(f"Fetching HTML content from {url}")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("HTML content fetched successfully")
        return html


# Part One: Extracting the "Information For" links
def extract_links(html):
    """
    Extracts the 'Information For' links from the HTML content.

    Args:
        html (bytes): The HTML content to extract links from.
    """
    soup = BeautifulSoup(html, 'html.parser')
    audience_nav = soup.find('div', id='audience-nav')
    if audience_nav is not None:
        print("Found 'audience-nav' section")
        links = audience_nav.find_all('a')
        for link in links:
            print(link)
    else:
        print("Could not find 'audience-nav' section")


# Part Two: Extracting the username and password fields from the login form
def extract_login_fields(html):
    """
    Extracts the username and password fields from the login form in the HTML content.

    Args:
        html (bytes): The HTML content to extract login form fields from.
    """
    soup = BeautifulSoup(html, 'html.parser')
    login_form = soup.find('div', id='login-form')
    if login_form is not None:
        print("Found 'login-form' section")
        username_field = login_form.find('input', {'id': 'login-username'})
        password_field = login_form.find('input', {'id': 'login-password'})

        print("Username field:", username_field)
        print("Password field:", password_field)
    else:
        print("Login form not found")


# Main function
def main():
    url = 'https://www.champlain.edu/current-students'
    html = fetch_html(url)

    print("Part One: Extracting 'Information For' links")
    extract_links(html)

    print("\nPart Two: Extracting login fields")
    extract_login_fields(html)


if __name__ == "__main__":
    main()
