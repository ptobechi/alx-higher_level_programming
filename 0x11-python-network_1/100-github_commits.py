#!/usr/bin/python3
"""
Script that lists 10 most recent commits (from the most recent to oldest)
of the repository “rails” by the user “rails” using the GitHub API.
Prints all commits by: <sha>: <author name> (one by line).
Uses the requests and sys packages.
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api/github.com/repos/{owner}/{repository}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits = response.json()[:10]

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name")

    except requests.exceptions.RequestException as err:
        print(err)
