# -*- coding: utf-8 -*-

import sys

start = {'F1': {'POG', 'THG', 'THM', 'PRG', 'RUG', 'RUM', 'COG', 'COM', 'E'},
         'F2': {'POM', 'PRM'},
         'F3': set([]),
          'F4': set([]),
         }
start = {'F1': {'E', 'HAM', 'LAM'},
         'F2': {'HAG'},
         'F3': {'LAG'},
         'F4': set([]),
         }

#0
start = {'F1': set([]),
         'F2': set([]),
         'F3': set([]),
         'F4': {'E', 'HAM', 'LAM', 'HAG', 'LAG'},
         }

#1
start = {'F1': set([]),
         'F2': set([]),
         'F3': {'E', 'HAM', 'LAM'},
         'F4': {'HAG', 'LAG'},
         }

#2
start = {'F1': set([]),
         'F2': set([]),
         'F3': {'HAM'},
         'F4': {'E', 'LAM', 'HAG', 'LAG'},
         }

#3
start = {'F1': set([]),
         'F2': set([]),
         'F3': {'E', 'HAG', 'HAM', 'LAG'},
         'F4': {'LAM'},
         }

#4
start = {'F1': set([]),
         'F2': set([]),
         'F3': {'HAG', 'LAG'},
         'F4': {'E', 'HAM', 'LAM'},
         }

#5
start = {'F1': set([]),
         'F2': set([]),
         'F3': {'E', 'HAM', 'LAM', 'HAG', 'LAG'},
         'F4': set([]),
         }

#6
start = {'F1': set([]),
         'F2': {'E', 'HAM', 'LAM'},
         'F3': {'HAG', 'LAG'},
         'F4': set([]),
         }

#7
start = {'F1': {'E', 'HAM', 'LAM'},
         'F2': set([]),
         'F3': {'HAG', 'LAG'},
         'F4': set([]),
         }


start = {'F1': {'POG', 'THG', 'THM', 'PRG', 'RUG', 'RUM', 'COG', 'COM', 'E'},
         'F2': {'POM', 'PRM'},
         'F3': set([]),
          'F4': set([]),
         }

# start = {'F1': {'E', 'HAM', 'LAM'},
#          'F2': {'HAG'},
#          'F3': {'LAG'},
#          'F4': set([]),
#          }

next_up = {'F1': 'F2',
             'F2': 'F3',
             'F3': 'F4',
             }

next_down = {'F4': 'F3',
               'F3': 'F2',
               'F2': 'F1',
               }

def print_floors(floors):
    for floor in ('F4', 'F3', 'F2', 'F1'):
        printable = '{:s} '.format(floor)
        for prefix in ('CO', 'PO', 'PR', 'RU', 'TH'):
            for item in ('G', 'M'):
                if prefix + item in floors[floor]:
                    printable += '{:s}{:s} '.format(prefix, item)
                else:
                    printable += '.   '
        if 'E' in floors[floor]:
            printable += 'E'
        else:
            printable += '.'
        print printable

def find_elevator(floors):
    for floor in floors.keys():
        if 'E' in floors[floor]:
            return floor
    raise ValueError('No Elevator')
    

def is_end_state(floors):
    for floor in ('F1', 'F2', 'F3'):
        if floors[floor]:
            return False

    return True

def validate_floors(floors):
    for val in floors.values():
        for item in val:
            if item.endswith('M') and item[:2] + 'G' in val:
                continue
            if item.endswith('M') and {x for x in val if x.endswith('G')}:
                return False
    return True

def validate_move(floors, target, item1, item2):
    if item1 is None and item2 is None:
        return False
    current_floor = find_elevator(floors)
    if target > current_floor:
        if target != next_up[current_floor]:
            return False
    else:
        if target != next_down[current_floor]:
            return False

    if item1 and item2:
        if item1[-1] != item2[-1] and item1[:2] != item2[:2]:
            return False

    return True

def combinations(l):
    if len(l) < 2:
        return []
    return [(l[0], x) for x in l[1:]] + combinations(l[1:])

def possible_moves(floors):
    current_floor = find_elevator(floors)
    items = list(floors[current_floor].difference({'E'}))
    the_combinations = combinations(items)
    possible_moves = []
    if current_floor in next_up:
        possible_moves.extend([(floors, next_up[current_floor], x, None) for x in items])
        possible_moves.extend([(floors, next_up[current_floor], x, y) for x, y in the_combinations])

    if current_floor in next_down:
        possible_moves.extend([(floors, next_down[current_floor], x, None) for x in items])
        possible_moves.extend([(floors, next_down[current_floor], x, y) for x, y in the_combinations])

    return possible_moves
                
def move(floors, target, item1, item2):
    current_floor = find_elevator(floors)
    if target > current_floor:
        next_floor = next_up[current_floor]
    else:
        next_floor = next_down[current_floor]

    new_floors = {x: floors[x].copy() for x in floors.keys()}
    new_floors[current_floor].remove('E')
    new_floors[next_floor].add('E')
    if item1:
        new_floors[current_floor].remove(item1)
        new_floors[next_floor].add(item1)
    if item2:
        new_floors[current_floor].remove(item2)
        new_floors[next_floor].add(item2)
    return new_floors

def hash_floors(floors):
    f4='.'.join(sorted(list(floors['F4'])))
    f3='.'.join(sorted(list(floors['F3'])))
    f2='.'.join(sorted(list(floors['F2'])))
    f1='.'.join(sorted(list(floors['F1'])))
    return 'F4:{:s}#F3:{:s}#F2:{:s}#F1{:s}'.format(f4, f3, f2, f1)

def path(floors):
    queue = [[floors]]
    visited = {hash_floors(floors)}
    while queue:
        if is_end_state(queue[0][-1]):
            return queue[0][1:]
        
        next_floors = []
        for a_move in possible_moves(queue[0][-1]):
            if validate_move(*a_move):
                candidate_floors = move(*a_move)
                candidate_floors_hash = hash_floors(candidate_floors)
                if validate_floors(candidate_floors) and candidate_floors_hash not in visited:
                    next_floors.append(queue[0] + [candidate_floors])
                    visited.add(hash_floors(candidate_floors))
        queue = queue[1:] + next_floors
    return []
            
l = path(start)
print l
print len(l)
