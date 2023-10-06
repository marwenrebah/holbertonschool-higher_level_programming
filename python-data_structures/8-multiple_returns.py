#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)
    c = ""
    if len == 0:
        c = None
    else:
        c = sentence[0]
    return (len, c)
