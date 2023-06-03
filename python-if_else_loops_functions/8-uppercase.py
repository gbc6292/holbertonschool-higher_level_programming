#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper = chr(ord(i) - 32)

        else:
            upper = i
        print("{}".format(upper), end='')
    print()
