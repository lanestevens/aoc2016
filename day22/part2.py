# -*- coding: utf-8 -*-

import hashlib
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
    

parse_name = re.compile('/dev/grid/node-x(?P<x>[0-9]+)-y(?P<y>[0-9]+)')
def node_coordinates(key):
    m = parse_name.match(key)
    return (int(m.groupdict()['x']), int(m.groupdict()['y']))

def node_key(coordinates):
    return '/dev/grid/node-x{0:d}-y{1:d}'.format(*coordinates)

def candidate_keys(key):
    coordinates = node_coordinates(key)
    keys = []
    if coordinates[0] > 0:
        keys.append(node_key((coordinates[0] - 1, coordinates[1])))
    if coordinates[1] > 0:
        keys.append(node_key((coordinates[0], coordinates[1] - 1)))
    keys.append(node_key((coordinates[0] + 1, coordinates[1])))
    keys.append(node_key((coordinates[0], coordinates[1] + 1)))
    return keys

def available_moves(grid, start_key):
    moves = []
    for candidate_key in candidate_keys(start_key):
        if candidate_key in grid and grid[candidate_key]['avail'] >= grid[start_key]['used']:
            moves.append(candidate_key)
    
    return moves

def start_node(grid):
    start = None
    for key in grid.keys():
        coords = node_coordinates(key)
        if coords[1]:
            continue
        
        if start is None:
            start = coords
        else:
            if start[0] < coords[0]:
                start = coords

    return node_key(start)

def make_move(grid, src, dst):
    return {src: {'used': 0,
                  'avail': grid[src]['used'] + grid[src]['avail'],
                  },
            dst: {'used': grid[dst]['used'] + grid[src]['used'],
                  'avail': grid[dst]['avail'] - grid[src]['used'],
                  },
            }

def apply_overrides(grid, overrides):
    return {key: overrides.get(key, grid[key]) for key in grid.keys()}

def steps(grid, target, start):
    q = [(grid, {}, start, [])]
    steps_len = 0
    while q:
        this_grid, current_overrides, data_location, current_steps = q[0]
        this_grid = apply_overrides(this_grid, current_overrides)
        # if steps_len != len(current_steps):
        #     #print len(current_steps)
        #     steps_len = len(current_steps)
        for key in this_grid.keys():
            for move in available_moves(this_grid, key):
                if key == data_location and move == target:
                    return current_steps + [(key, move)]
                if (key, move) in current_steps:
                    continue
                if key == data_location:
                    q.append((this_grid, make_move(this_grid, key, move), move, current_steps + [(key, move)]))
                else:
                    q.append((this_grid, make_move(this_grid, key, move), data_location, current_steps + [(key, move)]))
        q = q[1:]
    

grid = populate_grid(sys.stdin.readlines()[2:])
print len(steps(grid, node_key((0,0)), start_node(grid)))

