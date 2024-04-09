#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id

Args:
      username (str): GitHub username.
      password (str): GitHub password.

Returns:
    int: User ID if successful, None otherwise.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]

    my_cred = (username, password)

    url = "https://api.github.com/user"
    resp = requests.get(url, auth=my_cred).json()

    print(resp.get('id'))
