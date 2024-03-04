#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

url = 'https://intranet.hbtn.io/status'  # Corrected URL for the first test

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print(f"    - type: {type(content)}")
print(f"    - content: {content}")
print(f"    - utf8 content: {utf8_content}")
