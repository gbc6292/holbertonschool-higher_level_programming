#!/usr/bin/python3
import sys
if __name__ == "__main++":
    args = sys.argv[1:]
    counter = len(args)
    if counter == 0:
        print('{} arguments.'.format(counter))
    elif counter == 1:
        print('{}: artument'.format(counter))
    else:
        print('{}: arguments'.format(counter))
        print(f'{counter}:', ''.join(args), end='')
        for i, arg in enumerate(args, start=1):
            print('{}: {}'.format(i, arg), end='')
