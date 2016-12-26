# -*- coding: utf-8 -*-

import sys
from collections import deque
from itertools import permutations

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

deltas = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def get_steps(map, start, goal):
    q = deque([(start, [])])
    seen = set([])
    while q:
        current, path = q.popleft()
        for dx, dy in deltas:
            x, y = current[0] + dx, current[1] + dy
            move = (x, y)
            if (x, y) == goal:
                return path + [move]
            if move in seen:
                continue
            try:
                if map[y][x] == '#':
                    continue
            except:
                continue
            seen.add(move)
            q.append((move, path + [move]))

    raise ValueError('No Path')

def pairwise_distances(map, goals):
    if len(goals) == 2:
        return [(goals[0], goals[1], len(get_steps(map, goals[0], goals[1])))]
    l = []
    start = goals[0]
    for goal in goals[1:]:
        l.append((start, goal, len(get_steps(map, start, goal))))
    return l + pairwise_distances(map, goals[1:])

def shortest_path(map, start, goals):
    distances = pairwise_distances(map, [start] + goals)
    distance_map = {(x, y): z for x, y, z in distances}
    distance_map.update({(y, x): z for x, y, z in distances})

    current_shortest_len = None
    for path in permutations(goals):
        steps = distance_map[(start, path[0])] + distance_map[(path[-1], start)]
        for stop in range(len(path) -1):
            steps += distance_map[(path[stop], path[stop + 1])]
        if current_shortest_len is None or steps < current_shortest_len:
            current_shortest_len = steps

    return current_shortest_len

map = gen_map(sys.stdin.readlines())
start = get_start(map)
goals = get_goals(map)
print shortest_path(map, start, goals)

