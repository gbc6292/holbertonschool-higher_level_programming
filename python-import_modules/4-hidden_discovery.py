#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    words = dir(hidden_4)
    words_filtered = []

    for name in words:
        if not name.startswith('__'):
            words_filtered.append(name)

    words_filtered.sort()

    for name in words_filtered:
        print(name)
