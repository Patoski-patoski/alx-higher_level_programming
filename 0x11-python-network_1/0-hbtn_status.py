#!/usr/bin/python3
""" The 0-hbtn_status Module """

if __name__ == "__main__":
    import urllib.request

# Define the URL
url = 'https://alx-intranet.hbtn.io/status'

# Fetch the URL using a with statement to ensure the response is properly closed
with urllib.request.urlopen(url) as response:
    # Read the content of the response
    content = response.read()
    print("Body response")

    # Print the type of the content
    print(" - type: {}".format(type(content)))

    # Print the content itself
    print(" - content: {}".format(content))

    # Decode the content to a string and print it
    content_str = content.decode('utf-8')
    print(" - utf8 content: {}".format(content_str))
