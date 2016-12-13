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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def decode(id):
    first = ord('a') - 1
    last = ord('z')
    coded_name = ' '.join([x for x in id.split('-')][:-1])
    cypher = sector_id(id) % 26
    decoded_name = ''
    for c in coded_name:
        if c == ' ':
            decoded_name += c
        else:
            this = ord(c) + cypher
            if this > last:
                this = first + (this - last)
            decoded_name += chr(this)
            
    return decoded_name
    
for line in sys.stdin.readlines():
    line = line.strip()
    if validate(line):
        name = decode(line)
        if name.startswith('north'):
            print name, sector_id(line)
