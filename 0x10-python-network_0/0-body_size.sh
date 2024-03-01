#!/bin/bash
# This script takes in a URL, sends a request, and displays the size of the body of the response

# Usage: ./0-body_size.sh <URL>

# Make the request with curl and display the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

