#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()
