# -*- coding: utf-8 -*-

import sys

def coordinate_type(x, y, z):
    if len([x for x in '{:b}'.format(x*x + 3*x + 2*x*y + y + y*y + z) if x == '1']) % 2:
        return 'wall'
    return 'open'

def print_space():
    printable = '  '
    for x in range(len(space[0])):
        printable += '{:d}'.format(x)
    print printable
    for y in range(len(space)):
        printable = '{:d} '.format(y)
        for x in range(len(space[0])):
            printable += space[y][x]
        print printable
    
def create_space(l, modifier, print_path=True):
    if l:
        max_x = max([x[0] for x in l])
        max_y = max([x[1] for x in l])
    else:
        max_x = max_y = 10
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            if print_path and (x, y) in l:
                this = 'O'
            else:
                this_coordinate = coordinate_type(x, y, modifier)
                this = '#' if this_coordinate == 'wall' else '.'
            row.append(this)
            
        space.append(row)
        
def possible_moves(point, modifier):
    the_x = point[0]
    the_y = point[1]

    the_moves = []
    for x in (the_x - 1, the_x, the_x + 1):
        for y in (the_y - 1, the_y, the_y + 1):
            if x < 0:
                continue
            if y < 0:
                continue
            if x == the_x or y == the_y:
                if coordinate_type(x, y, modifier) == 'open' and (x, y) != point:
                    the_moves.append((x, y))
    return the_moves
            
def paths(start, end, modifier):
    queue = [[start]]
    visited = {start}
    while queue:
        new_paths = []
        for next_move in possible_moves(queue[0][-1], modifier):
            if next_move in queue[0]:
                continue
            if next_move in visited:
                continue
            if len(queue[0]) >= 51:
                continue
            new_paths.append(queue[0] + [next_move])
            visited.add(next_move)
        queue = queue[1:] + new_paths
    return visited

        
space = []
# l = paths((1,1), (7,4), 10)
# print l
# print len(l) - 1
# create_space(l, 10)
# print_space()

visited = paths((1,1), (31, 39), 1350)
print len(visited)
print visited
#create_space(l, 1350)
#print_space()
#print l
#print len(l) - 1
