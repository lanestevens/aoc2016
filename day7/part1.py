# -*- coding: utf-8 -*-

import re
import sys

def abba(segment):
    for i in range(1, len(segment) - 2):
        if segment[i] == segment[i + 1] and segment[i - 1] == segment[i + 2] and segment[i - 1] != segment[i]:
            return True
    return False
        
def valid(ip):
    out = True
    is_abba = False
    for segment in re.findall('([a-z]+)', ip):
        if not out and abba(segment):
            return False
        if out and abba(segment):
            is_abba = True
        out = not out
    return is_abba

count = 0
for line in sys.stdin.readlines():
    line = line.strip()
    if valid(line):
        count += 1

print count

    
