#!/bin/bash
# This script takes in a URL, sends a GET request with a header, and displays the body of the response

# Usage: ./4-header.sh <URL>

# Make a GET request with a custom header and display the response body
curl -s -H "X-School-User-Id: 98" "$1"

