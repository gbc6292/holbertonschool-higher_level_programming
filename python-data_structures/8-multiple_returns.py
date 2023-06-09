#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == "":
        len1 = len(sentence)
        char = None
        return len1, char

    len1 = len(sentence)

    char = sentence[0]

    return len1, char
