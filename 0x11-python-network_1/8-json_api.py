#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"
    q = argv[1]

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    try:
        resp = requests.post(url, data={'q': q})
        data = resp.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
