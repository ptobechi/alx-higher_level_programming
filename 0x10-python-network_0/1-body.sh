#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -sL -w "%{http_code}" "$1" -o /dev/null | awk '{if($1 == 200) system("curl -sL "$1)}'
