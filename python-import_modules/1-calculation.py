#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = 5
    b = 10
    s = add(a, b)
    z = sub(a, b)
    m = mul(a, b)
    d = div(a, b)
print('{} + {} = {}'.format(a, b, s))
print('{} - {} = {}'.format(a, b, z))
print('{} * {} = {}'.format(a, b, m))
print('{} / {} = {}'.format(a, b, d))
