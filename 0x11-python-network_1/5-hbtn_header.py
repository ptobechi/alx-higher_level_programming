#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the value of the variable X-Request-Id in the response header.
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Check if X-Request-Id is present in the response headers
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
