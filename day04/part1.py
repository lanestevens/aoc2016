# -*- mode: Python -*-

import re
import sys

def checksum(map):
    return ''.join([x[1] for x in sorted([(-y, x) for x, y in map.items()])[:5]])

def sector_id(id):
    return int(id.split('-')[-1][:-7])

def validate(id):
    map = {}
    parts = [x for x in id.split('-') if 'a' <= x[0] <= 'z']
    for c in ''.join(parts):
        if c not in map:
            map[c] = 1
        else:
            map[c] += 1

    if checksum(map) == id[-6:-1]:
        return True
    return False


sum = 0
for line in sys.stdin.readlines():
    line = line.strip()
    if validate(line):
        sum += sector_id(line)
print sum
