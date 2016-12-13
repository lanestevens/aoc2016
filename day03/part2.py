# -*- mode: Python -*-

import sys


goods = 0
lines = sys.stdin.readlines()
while lines:
    a1, b1, c1 = [int(x) for x in lines[0].split()]
    a2, b2, c2 = [int(x) for x in lines[1].split()]
    a3, b3, c3 = [int(x) for x in lines[2].split()]
    lines = lines[3:]
    if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
        goods += 1
    if b1 + b2 > b3 and b1 + b3 > b2 and b2 + b3 > b1:
        goods += 1
    if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
        goods += 1

print goods


