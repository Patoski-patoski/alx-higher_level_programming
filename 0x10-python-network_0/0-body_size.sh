#!/usr/bin/env bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response


# Send a request to the URL and get the Content-Length Header
curl -sI  "$1" | awk '/Content-Length/ {print $2}'
