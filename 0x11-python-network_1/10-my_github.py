#!/usr/bin/python3
""" a Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]

    my_cred = (username, password)

    url = "https://api.github.com/user"
    resp = requests.post(url, auth=my_cred)

    if resp.status_code == 200:
        user_id = resp.json().get('id')
        print(user_id)
    else:
        print(None)
