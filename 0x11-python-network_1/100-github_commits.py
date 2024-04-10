#!/usr/bin/python3
"""A Python script that list 10 commits (from the most recent to oldest) of
the repository
"""
import sys
import requests


if __name__ == "__main__":
    from sys import argv
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])

    commits = requests.get(url).json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
