#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
#!/bin/bash

curl -s -I -X OPTIONS $1 | awk '/^Allow:/ {sub(/^Allow: /, "", $0); print}'
