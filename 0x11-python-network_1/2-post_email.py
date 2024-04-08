#!/usr/bin/python3
""" 2-post_email: a Python script that takes in a URL and an email, sends a
    POST request to the passed URL with the email as a parameter, and displays
    the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse
    from urllib.parse import urlencode

    # Prepare the data
    data = {'email': argv[2]}
    data_encoded = urlencode(data).encode('utf-8')

    # Create the request object
    url = argv[1]
    my_request = request.Request(url, data=data_encoded, method='POST')

    # Send the request
    with request.urlopen(my_request) as response:
        content = response.read()
        content_str = content.decode('utf-8')
        print(content_str)
