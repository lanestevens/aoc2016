# -*- mode: Python -*-

import sys

goods = 0
for line in sys.stdin.readlines():
    a, b, c = [int(x) for x in line.split()]
    if a + b > c and a + c > b and b + c > a:
        goods += 1
print goods


