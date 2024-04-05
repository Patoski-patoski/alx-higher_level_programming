#!/usr/bin/env bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response

curl -Is patoski.tech > page.txt
awk '/^Content-Length: / {print substr($0, 17)}' page.txt