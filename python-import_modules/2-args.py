#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    counter = len(args)
    if counter == 0:
        print('{} arguments.'.format(counter))
    elif counter == 1:
        print('{}: argument'.format(counter))
    else:
        print('{}: arguments'.format(counter), end='')
        print(f'{counter}:', ''.join(args), end='')
        for i, arg in enumerate(args, start=1):
            print('{}: {}'.format(i, arg), end='')
