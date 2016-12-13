# -*- coding: utf-8 -*-

import sys

screen = [[0 for x in range(50)] for y in range(6)]
#screen = [[0 for x in range(7)] for y in range(3)]

def disp():
    for row in screen:
        print ''.join(['1' if x else ' ' for x in row])

def rect(cols, rows):
    for row in range(rows):
        for col in range(cols):
            screen[row][col] = 1

def rotate_row(row, pixels):
    pixels = pixels % len(screen[0])
    if pixels == 0:
        return
    the_row = screen[row]
    screen[row] = the_row[-pixels:] + the_row[:-pixels]

def rotate_column(col, pixels):
    pixels = pixels % len(screen)
    if pixels == 0:
        return
    the_column = [x[col] for x in screen]
    the_column = the_column[-pixels:] + the_column[:-pixels]
    for i in range(len(screen)):
        screen[i][col] = the_column[i]
    
for line in sys.stdin.readlines():
    if line.startswith('rect'):
        rows, cols = [int(x) for x in line.split(' ')[1].split('x')]
        rect(rows, cols)
    elif line.startswith('rotate row'):
        row, cols = [int(x) for x in line.split('=')[1].split(' by ')]
        rotate_row(row, cols)
    elif line.startswith('rotate column'):
        col, rows = [int(x) for x in line.split('=')[1].split(' by ')]
        rotate_column(col, rows)
        
count = 0
for row in screen:
    count += sum(row)

disp()
print count
