#!/bin/bash
# Bash script that sends a JSON POST request to a URL and displays the body of the response

url=$1
json_file=$2

# Check if the file contains valid JSON
if jq . "$json_file" >/dev/null 2>&1; then
    # Send POST request and display response body
    curl -sX POST -H "Content-Type: application/json" -d @"$json_file" "$url"
else
    echo "Not a valid JSON"
fi

