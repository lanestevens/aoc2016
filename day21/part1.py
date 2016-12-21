# -*- coding: utf-8 -*-

import re
import sys

p = 'abcdefgh'

def swap_position(s, x, y):
    if y < x:
        x, y = y, x
    return s[:x] + s[y] + s[x + 1:y] + s[x] + s[y+1:]

def swap_letters(s, cx, cy):
    x = s.find(cx)
    y = s.find(cy)
    return swap_position(s, x, y)

def rot_left(s, x):
    x = x % len(s)
    return s[x:] + s[:x]

def rot_right(s, x):
    x = x % len(s)
    return s[len(s) - x:] + s[:len(s) - x]

def rev(s, x, y):
    return s[:x] + s[x:y + 1][::-1] + s[y + 1:]

def rot_letter(s, cx):
    x = s.find(cx)
    s = rot_right(s, 1)
    s = rot_right(s, x)
    if x >= 4:
        s = rot_right(s, 1)
    return s

def mov_x_y(s, x, y):
    if y < x:
        return s[:y] + s[x] + s[y:x] + s[x + 1:]
    return s[:x] + s[x + 1:y + 1] + s[x] + s[y + 1:]

swap_position_re = re.compile('swap position (?P<x>[0-9]+) with position (?P<y>[0-9]+)')
swap_letters_re = re.compile('swap letter (?P<cx>.) with letter (?P<cy>.)')
rot_left_re = re.compile('rotate left (?P<x>[0-9]+) steps?')
rot_right_re = re.compile('rotate right (?P<x>[0-9]+) steps')
rot_position_re = re.compile('rotate based on position of letter (?P<cx>.)')
rev_re = re.compile('reverse positions (?P<x>[0-9]+) through (?P<y>[0-9]+)')
mov_re = re.compile('move position (?P<x>[0-9]+) to position (?P<y>[0-9]+)')
instructions = (swap_position_re, swap_letters_re, rot_left_re, rot_right_re, rot_position_re, rev_re, mov_re)

def scramble(s, i):
    for instruction in instructions:
        m = instruction.match(i)
        if m:
            this_instruction = instruction
            break

    if this_instruction == swap_position_re:
        return swap_position(s, int(m.groupdict()['x']), int(m.groupdict()['y']))
    if this_instruction == swap_letters_re:
        return swap_letters(s, m.groupdict()['cx'], m.groupdict()['cy'])
    if this_instruction == rot_left_re:
        return rot_left(s, int(m.groupdict()['x']))
    if this_instruction == rot_right_re:
        return rot_right(s, int(m.groupdict()['x']))
    if this_instruction == rot_position_re:
        return rot_letter(s, m.groupdict()['cx'])
    if this_instruction == rev_re:
        return rev(s, int(m.groupdict()['x']), int(m.groupdict()['y']))
    if this_instruction == mov_re:
        return mov_x_y(s, int(m.groupdict()['x']), int(m.groupdict()['y']))

def combinations(s, low=0):
    if low + 1 > len(s):
        yield s
    else:
        for p in combinations(s, low + 1):
            yield p
        for i in range(low + 1, len(s)):
            s[low], s[i] = s[i], s[low]
            for p in combinations(s, low + 1):
                yield p
            s[low], s[i] = s[i], s[low]


all_instructions = [x.strip() for x in sys.stdin.readlines()]
for combo in combinations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
    p = ''.join(combo)
    for instruction in all_instructions:
        p = scramble(p, instruction)
    if p == 'fbgdceah':
        break
print ''.join(combo)
