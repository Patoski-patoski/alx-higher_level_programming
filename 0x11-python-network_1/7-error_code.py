#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
    displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        response = requests.get(argv[1])
        # This will raise an HTTPError if the response was an HTTP error
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as http_err:
        print(f"Error code: {http_err.response.status_code}")
