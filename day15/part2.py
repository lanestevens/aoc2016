# -*- coding: utf-8 -*-

import sys

discs = [(1, 13),
         (10, 19),
         (2, 3),
         (1, 7),
         (3, 5),
         (5, 17),
         (0, 11),
         ]

def advance_time(l):
    new_l = []
    for item in l:
        new_l.append(((item[0] + 1) % item[1], item[1]))
    return new_l

def check_slots(l):
    current = l[:]
    for i in range(len(l)):
        current = advance_time(current)
        if current[i][0]:
            return False

    return True

def find_time(l):
    i = 0
    while True:
        if check_slots(l):
            return i
        l = advance_time(l)
        i += 1

print find_time(discs)

         
