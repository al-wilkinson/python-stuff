#!/usr/bin/env python3
"""Module: retrieve IP addresses from given url"""

import re
import requests

def extract_ip_addresses(text):
    """Function: extract IP addresses from retrieved web page"""
    ip_pattern = r'\b(?:\d{1,3}\.\d{1,3}\.\d{1,3}\[.\]\d{1,3})\b'
    # Find all IP addresses in the text using the regular expression
    ip_addrs = re.findall(ip_pattern, text)
    return ip_addrs

def get_web_page(url):
    """Function: retrieve the web page"""
    timeout = 30
    try:
        # Send an HTTP GET request to fetch the web page content
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an exception for any unsuccessful request

        # Return the web page content
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching the web page:", e)
        return None

if __name__ == "__main__":
    # Replace the URL below with the web page you want to fetch
    URL_TO_FETCH = "https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/"
    # Get the web page content
    web_page_content = get_web_page(URL_TO_FETCH)
    if web_page_content:
        # Extract IP addresses from the web page content
        ip_addresses = extract_ip_addresses(web_page_content)
        # Print the list of IP addresses found
        # print(web_page_content)
        print("IP Addresses:")
        for ip in ip_addresses:
            characters_to_remove = ['[',']']
            for char in characters_to_remove:
                ip = ip.replace(char, '')

            print('"' + ip + '", ', end='')
    else:
        print("Failed to fetch the web page.")
