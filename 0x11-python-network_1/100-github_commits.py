#!/usr/bin/python3
"""A Python script that list 10 commits (from the most recent to oldest) of
the repository
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])

    commits = requests.get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
