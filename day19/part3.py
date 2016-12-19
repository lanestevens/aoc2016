# -*- coding: utf-8 -*-

elves = [(x + 1, 1) for x in range(3014603)]
#elves = [(x + 1, 1) for x in range(5)]

def find_left(l, i):
    half = len(l) / 2
    target = i + half
    if target >= len(l):
        target = target - len(l)
    return target

def cycle(l):
    i = 0
    while i < len(l):
        j = find_left(l, i)
        if j == i:
            break
        l[i] = (l[i][0], l[i][1] + l[j][1])
        del(l[j])
        if j > i:
            i += 1

while True:
    cycle(elves)
    if len(elves) == 1:
        break
print elves[0][0]
