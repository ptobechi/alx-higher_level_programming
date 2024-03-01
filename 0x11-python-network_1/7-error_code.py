#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response. If the HTTP status code is greater than or
equal to 400, it prints: Error code: followed by the value of the HTTP
status code.
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
