# -*- coding: utf-8 -*-

import hashlib

open_doors = {'b', 'c', 'd', 'e', 'f'}
def valid_moves(passcode, current_path, position):
    hash = hashlib.md5(passcode + current_path).hexdigest()
    the_moves = []
    if hash[0] in open_doors and position[1] > 0:
        the_moves.append('U')
    if hash[1] in open_doors and position[1] < 3:
        the_moves.append('D')
    if hash[2] in open_doors and position[0] > 0:
        the_moves.append('L')
    if hash[3] in open_doors and position[0] < 3:
        the_moves.append('R')

    return the_moves

def next_location(current_position, direction):
    if direction == 'U':
        return (current_position[0], current_position[1] - 1)
    if direction == 'D':
        return (current_position[0], current_position[1] + 1)
    if direction == 'L':
        return (current_position[0] - 1, current_position[1])
    if direction == 'R':
        return (current_position[0] + 1, current_position[1])
    raise ValueError('Unknown Direction:  {:s}'.format(direction))

def get_path(passcode):
    queue = [((0,0), '')]
    while queue:
        current_position, current_path = queue[0]
        for move in valid_moves(passcode, current_path, current_position):
            the_next_location = next_location(current_position, move)
            if the_next_location == (3, 3):
                last_solution = current_path + move
            else:
                queue.append((the_next_location, current_path + move))
        queue = queue[1:]
    return last_solution

#print get_path('ihgpwlah')
#print get_path('kglvqrro')
#print get_path('ulqzkmiv')
print len(get_path('ioramepc'))
