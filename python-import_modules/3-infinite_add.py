#!/usr/bin/python3

import sys


if __name__ == "__main__":

    args = sys.argv[1:]

    nums = []
    for i in args:
        nums.append(int(i))

    total = sum(nums)
    print(total, end="\n")
