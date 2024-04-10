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
    commits = resp.json()

    for commit in commits[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
