#!/usr/bin/python3
""" a Python script that takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a parameter, and
    finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    my_data = {'email': argv[2]}
    resp = requests.post(argv[1], data=my_data)

    print(resp.text)
