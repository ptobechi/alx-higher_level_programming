#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept

# Usage: ./3-methods.sh <URL>

# Make an OPTIONS request to get allowed methods and display them
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-

