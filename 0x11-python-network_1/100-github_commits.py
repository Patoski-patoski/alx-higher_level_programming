#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge

Arg:
    argv[1]: repository name
    argv[2]: owner_name

Return:
    10 commits sha and owner names
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{username}/{owner_name}/commits"
    resp = requests.get(url)

    info = resp.json()

    for i in range(10, 0, -1):
        commit_data = resp.json()[i]
        commit_sha = commit_data.get('sha')
        commiter_name = commit_data.get('commit').get('author').get('name')
        print(f"{commit_sha}: {commiter_name}")
