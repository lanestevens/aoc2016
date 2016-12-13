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

def navigate(directions):
    current_x = 0
    current_y = 0
    current_direction = N
    for turn, distance in [(x[0], int(x[1])) for x in re.findall('([RL])([0-9]+),?', directions)]:
        current_direction = next_directions[current_direction][turn]
        if current_direction in (N,S):
            current_y += distance if current_direction == N else -distance
        else:
            current_x += distance if current_direction == E else -distance

    return abs(current_x) + abs(current_y)

print navigate('R2, L3')
print navigate('R2, R2, R3')
print navigate('R5, L5, R5, R3')
print navigate('R2, R2, R2, R2')
print navigate('R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3, R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4')


        
