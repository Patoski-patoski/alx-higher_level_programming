#!/usr/bin/env python3

result = ""
store = 0
for char in range(ord('z'), ord('a') - 1, -1):
    if store % 2 == 0:
        result += "{}".format(chr(char))
        store += 1
    else:
        result += "{}".format(chr(char - 32))
        store += 1

print(result, end="")
