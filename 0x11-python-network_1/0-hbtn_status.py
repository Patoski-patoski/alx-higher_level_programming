#!/usr/bin/python3
""" The 0-hbtn_status Module """

if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        print(f"Body response:")
        content = response.read()
        print(f"-type: {type(content)}")
        print(f"-content: {content}")
        print(f"-utf8 content: {content.decode('utf-8')}")
