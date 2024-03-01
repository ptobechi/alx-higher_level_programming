#!/bin/bash
# This script sends a DELETE request to the specified URL and displays the body of the response

# Usage: ./2-delete.sh <URL>

# Make the DELETE request with curl and display the body
curl -sX DELETE "$1"

