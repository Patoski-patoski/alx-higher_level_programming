#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """

import requests

req = requests.get("https://alx-intranet.hbtn.io/status")
content = req.text

print('Bad response:')
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
