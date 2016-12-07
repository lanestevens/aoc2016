# -*- mode: Python -*-

import re

N = 'N'
E = 'E'
S = 'S'
W = 'W'
L = 'L'
R = 'R'
next_directions = {N: {L: W, R: E},
                   E: {L: N, R: S},
                   S: {L: E, R: W},
                   W: {L: S, R: N},
                   }

def stops(direction, current_x, current_y, distance):
    if direction == N:
        return [(current_x, y) for y in range(current_y + 1, current_y + 1 + distance)]
    if direction == S:
        return [(current_x, y) for y in range(current_y - 1, current_y - 1 - distance, -1)]
    if direction == E:
        return [(x, current_y) for x in range(current_x + 1, current_x + 1 + distance)]
    if direction == W:
        return [(x, current_y) for x in range(current_x - 1, current_x - 1 - distance, -1)]
    return []

def navigate(directions):
    current_x = 0
    current_y = 0
    current_direction = N
    position_history = [(0, 0)]
    for turn, distance in [(x[0], int(x[1])) for x in re.findall('([RL])([0-9]+),?', directions)]:
        current_direction = next_directions[current_direction][turn]
        for stop in stops(current_direction, current_x, current_y, distance):
            if stop in position_history:
                return abs(stop[0]) + abs(stop[1])
            position_history.append(stop)
            current_x = stop[0]
            current_y = stop[1]

    return abs(current_x) + abs(current_y)

print navigate('R8, R4, R4, R8')
print navigate('R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3, R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4')


        
