#!/usr/bin/python3
""" The 0-hbtn_status Module """

if __name__ == "__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

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
