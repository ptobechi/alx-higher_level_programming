#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user ID.
Uses Basic Authentication with a personal access token as the password to
access user information (only read:user permission is needed).
The first argument will be the username.
The second argument will be the password (personal access token).
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, password))
        response.raise_for_status()

        try:
            user_data = response.json()
            print(user_data['id'])
        except ValueError:
            print("None")
    except requests.exceptions.RequestException as err:
        print(err)
