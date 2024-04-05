#!/usr/bin/env bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

#Send a request to the URL and get the Content-Length Header

content_length=$(curl -sI  "$1" | grep -i Content-Length | awk '{print $2}')

#Check if Content-Length is found

if [ -z "$content_length" ]; then
	echo "Content-Length not found in the response."
	exit 1
fi

echo "$content_length"
