#!/usr/bin/python3
""" The 0-hbtn_status Module """

if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
