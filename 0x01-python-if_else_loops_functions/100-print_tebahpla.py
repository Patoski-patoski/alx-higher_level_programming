#!/usr/bin/env python3

for char in range(122, 96, -1):
    if char % 2:
        char -= 32
    print(chr(char), end="")
