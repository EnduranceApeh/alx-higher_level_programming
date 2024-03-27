#!/bin/bash
# Bash script that takes in a URL
# sends a request to that URL
# Displays the size of the body of the response

URL=$1
curl -sI "$URL" | grep 'Content-Length:' | cut -f2 -d' '
