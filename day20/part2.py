# -*- coding: utf-8 -*-

import sys

blocked_ips = []

def add_range(the_range):
    low, high = [int(x) for x in the_range.split('-')]
    if blocked_ips == []:
        blocked_ips.append((low, high))
        return

    for range_low, range_high in blocked_ips:
        if low < range_low and high >= range_low:
            blocked_ips.append((low, max(high, range_high)))
            return

        if range_low <= low <= range_high:
            blocked_ips.append((min(low, range_low), max(high, range_high)))
            return

    blocked_ips.append((low, high))

def merge_ranges(l):
    while True:
        changed = False
        merged_list = []
        i = 0
        while i < len(l):
            if i == len(l) - 1:
                merged_list.append(l[i])
            elif l[i][1] >= l[i + 1][0] - 1:
                merged_list.append((min(l[i][0], l[i + 1][0]), max(l[i][1], l[i + 1][1])))
                changed  = True
                i += 1
            else:
                merged_list.append(l[i])
            i += 1
        if not changed:
            return merged_list
        l = merged_list

def count_gaps(l):
    count = 0
    for i in range(len(l)):
        if i == len(l) - 1:
            continue
        count += (l[i + 1][0] - (l[i][1] + 1))

    return count
    
# test_data = ['5-8', '0-2', '4-7']
# for the_range in test_data:
#     add_range(the_range)
for the_range in sys.stdin.readlines():
    add_range(the_range)

print count_gaps(merge_ranges(sorted(blocked_ips)))


