#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
# causing the server to respond with "You got me!" in the body of the response

curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"

