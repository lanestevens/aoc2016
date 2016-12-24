# -*- coding: utf-8 -*-

import hashlib
import re
import sys

parse_name = re.compile('/dev/grid/node-x(?P<x>[0-9]+)-y(?P<y>[0-9]+)')
def node_coordinates(key):
    m = parse_name.match(key)
    return (int(m.groupdict()['x']), int(m.groupdict()['y']))

def node_key(coordinates):
    return '/dev/grid/node-x{0:d}-y{1:d}'.format(*coordinates)

def populate_grid(lines):
    holding_tank = []
    max_x = 0
    max_y = 0
    for line in lines:
        node, size, used, avail, pct = line.strip().split()
        x, y = node_coordinates(node)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        used = int(used[:-1])
        avail = int(avail[:-1])
        holding_tank.append((x, y, used, avail))

    grid = []
    for y in range(max_y + 1):
        grid.append(range(max_x + 1))
        
    for x, y, used, avail in holding_tank:
        grid[y][x] = (used, avail, used + avail)

    return grid

def neighbors(x, y):
    the_neighbors = []
    if x > 0:
        the_neighbors.append((x - 1, y))
    if y > 0:
        the_neighbors.append((x, y - 1))
    return the_neighbors + [(x + 1, y), (x, y + 1)]

def available_moves(grid, x, y):
    moves = []
    for new_x, new_y in neighbors(x, y):
        if new_y >= len(grid):
            continue
        if new_x >= len(grid[y]):
            continue
        if grid[new_y][new_x][1] >= grid[y][x][0] and grid[y][x][0] > 0:
            moves.append((new_x, new_y))

    return moves

def start_node(grid):
    return (len(grid[0]) - 1, 0)

def make_move(grid, src, dst):
    dsrc = grid[src[1]][src[0]]
    ddst = grid[dst[1]][dst[0]]
    grid[dst[1]][dst[0]] = (ddst[0] + dsrc[0], ddst[1] - dsrc[0], ddst[2])
    grid[src[1]][src[0]] = (0, dsrc[2], dsrc[2])
    return grid

def copy_grid(grid):
    return [[grid[y][x] for x in range(len(grid[y]))] for y in range(len(grid))]

def steps(grid, target, start):
    q = [(grid, start, [])]
    printed = 0
    while q:
        this_grid, data_location, current_steps = q[0]
        if len(current_steps) != printed:
            printed = len(current_steps)
            print printed
        for y in range(len(this_grid)):
            for x in range(len(this_grid[y])):
                for move in available_moves(this_grid, x, y):
                    if (x, y) == data_location and move == target:
                        return current_steps + [(x, y)]
                    if current_steps and (move, (x,y)) == current_steps[-1]:
                        continue
                    if (x, y) == data_location:
                        q.append((make_move(copy_grid(this_grid), (x, y), move), move, current_steps + [((x,y), move)]))
                    else:
                        q.append((make_move(copy_grid(this_grid), (x, y), move), data_location, current_steps + [((x,y), move)]))
        q = q[1:]
        
grid = populate_grid(sys.stdin.readlines()[2:])
# from pprint import pprint
# pprint(grid)
# import pprint
# pprint.pprint(grid)
# pprint.pprint(copy_grid(grid))
print len(steps(grid, (0, 0), start_node(grid)))

