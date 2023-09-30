#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    letter = chr(a)
    if letter not in ['q', 'e']:
        print(letter, end="")
