# -*- coding: utf-8 -*-

import sys
counts = {}

for line in sys.stdin.readlines():
    line = line.strip()
    for i in range(len(line)):
        c = line[i]
        if i not in counts:
            counts[i] = {}
        if c not in counts[i]:
            counts[i][c] = 1
        else:
            counts[i][c] += 1

msg = ''
for i in range(len(counts)):
    l = sorted([(y, x) for x, y in counts[i].items()])
    msg += l[0][1]
print msg
