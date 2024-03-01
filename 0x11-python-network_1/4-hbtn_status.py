#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status.
Uses the requests package.
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
content_type = type(response.text)

print("Body response:")
print(f"    - type: {content_type}")
print(f"    - content: {response.text}")
