#!/bin/bash
# Bash script that sends a request to a URL and displays only the status code
echo $(curl -s -o /dev/null -w "%{http_code}" "$1")
