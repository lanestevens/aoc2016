# -*- coding: utf-8 -*-

import sys
from collections import deque

def gen_map(lines):
    rows = []
    for line in lines:
        rows.append(line.strip())

    return rows

def get_goals(map):
    goals = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in {'0', '.', '#'}:
                continue
            goals.append((x,y))
    return goals

def get_start(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '0':
                return (x, y)

def get_possible_moves(map, x, y):
    all_moves = []
    if x > 0:
        all_moves.append((x - 1, y))
    if y > 0:
        all_moves.append((x, y - 1))
    if x + 1 < len(map[y]):
        all_moves.append((x + 1, y))
    if y + 1 < len(map):
        all_moves.append((x, y + 1))

    return [(x, y) for x, y in all_moves if map[y][x] != '#']

def get_steps(map, goals, start):
    q = deque([(goals, start, [], [])])
    while q:
        goals, location, goal_steps, steps = q.popleft()
        for move in get_possible_moves(map, location[0], location[1]):
            if len(goals) == 1 and move in goals:
                return steps + [move]
            if move in goal_steps:
                continue
            if move in goals:
                q.append(([x for x in goals if x != move], move, [], steps + [move]))
            else:
                q.append((goals, move, goal_steps + [move], steps + [move]))

map = gen_map(sys.stdin.readlines())
print len(get_steps(map, get_goals(map), get_start(map)))

