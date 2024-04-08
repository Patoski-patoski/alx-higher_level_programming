#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        response = request.urlopen(argv[1])
        content = response.read()
        content_str = content.decode('utf-8')
        print(content_str)

    except error.URLError as err:
        print(f"Error code: {err.code}")
