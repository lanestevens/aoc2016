# -*- coding: utf-8 -*-

import re
import sys

def populate_grid(lines):
    grid = {}
    for line in lines:
        node, size, used, avail, pct = line.strip().split()
        if used[-1] != 'T' or avail[-1] != 'T':
            print line
        grid[node] = {'used': int(used[:-1]),
                      'avail': int(avail[:-1]),
                      }

    return grid

def count_pairs(grid):
    count = 0
    for a, a_vals in grid.iteritems():
        for b, b_vals in grid.iteritems():
            if a == b:
                continue
            if a_vals['used'] and a_vals['used'] <= b_vals['avail']:
                count += 1
    return count
    

print count_pairs(populate_grid(sys.stdin.readlines()[2:]))
