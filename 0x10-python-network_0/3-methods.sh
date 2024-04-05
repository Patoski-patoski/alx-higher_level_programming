#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
#!/bin/bash

url=$1

# Send an OPTIONS request to the URL and store the response headers in a variable
response=$(curl -s -I -X OPTIONS $url)

# Extract the Allow header from the response
allow_header=$(echo "$response" | grep -i '^Allow:' | tr -d '\r')

# Extract the allowed methods from the Allow header
allowed_methods=$(echo "$allow_header" | cut -d ' ' -f 2-)

# Display the allowed methods
echo $allowed_methods
