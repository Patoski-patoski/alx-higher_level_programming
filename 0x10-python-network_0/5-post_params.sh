#!/bin/bash
# a Bash script that sends a POST request to the passed URL, and displays the response
curl -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
