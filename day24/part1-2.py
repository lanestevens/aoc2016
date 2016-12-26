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

move_deltas = {(-1, 0), (1, 0), (0, -1), (0, 1)}
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
    max_x = len(map[0])
    max_y = len(map)
    q = deque([(goals, start, [], [])])
    goal_len = len(goals)
    steps_len = 0
    while q:
        goals, location, goal_steps, steps = q.pop()
        if len(goals) < goal_len:
            goal_len = len(goals)
            print 'Goals: ', goal_len
        for dx, dy in move_deltas:
            new_x = location[0] + dx
            new_y = location[1] + dy
            if new_x < 0 or new_x >= max_x:
                continue
            if new_y < 0 or new_y >= max_y:
                continue
            if map[new_y][new_x] == '#':
                continue
            move = (new_x, new_y)

            if [move] == goals:
                return steps + [move]
            if move in goal_steps:
                continue
            if move in steps:
                continue
            if move in goals:
                q.append(([x for x in goals if x != move], move, [], steps + [move]))
            else:
                q.append((goals, move, goal_steps + [move], steps + [move]))

map = gen_map(sys.stdin.readlines())
print len(get_steps(map, get_goals(map), get_start(map)))
