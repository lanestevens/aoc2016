# -*- coding: utf-8 -*-

elves = [(x + 1, 1) for x in range(3014603)]
elves = [(x + 1, 1) for x in range(5)]

def find_left(l, i, num_elves):
    half = num_elves / 2
    j = i
    while half:
        j += 1
        if j == num_elves:
            j = 0
        if l[j][1]:
            half += -1
    return j

def cycle(l, num_elves):
    for i in range(num_elves):
        if l[i][1] == 0:
            continue
        j = find_left(l, i, num_elves)
        l[i] = (l[i][0], l[i][1] + l[j][1])
        l[j] = (l[j][0], 0)
        num_elves += -1
        if num_elves == 1:
            return 1
    return num_elves

num_elves = len(elves)
while True:
    num_elves = cycle(elves, num_elves)
    if num_elves == 1:
        break
for i in range(len(elves)):
    if l[i][1]:
        print l[i][0]
