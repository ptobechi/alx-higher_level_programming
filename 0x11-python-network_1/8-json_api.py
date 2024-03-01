#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q. If no argument is
given, set q="".
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>.
Otherwise:
- Display "Not a valid JSON" if the JSON is invalid.
- Display "No result" if the JSON is empty.
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        try:
            json_data = response.json()
            if json_data:
                print(f"[{json_data['id']}] {json_data['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as err:
        print(err)
