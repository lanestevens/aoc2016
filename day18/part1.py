# -*- coding: utf-8 -*-

first_row = '^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^'
max_rows = 40

def next_row(prior_row):
    the_row = ''
    for i in range(len(prior_row)):
        left = '.' if i == 0 else prior_row[i - 1]
        center = prior_row[i]
        right = '.' if i == len(prior_row) - 1 else prior_row[i + 1]

        this = '.'
        lcr = left + center + right
        if lcr == '^^.':
            this = '^'
        if lcr == '.^^':
            this = '^'
        if lcr == '^..':
            this = '^'
        if lcr == '..^':
            this = '^'
        the_row += this
    return the_row

def get_tiles(first_row, max_rows):
    tiles = [first_row]
    prior_row = first_row
    for i in range(max_rows - 1):
        prior_row = next_row(prior_row)
        tiles.append(prior_row)
        
    return tiles

def count_safe_tiles(tiles):
    count = 0
    for tile in tiles:
        count += len([x for x in tile if x == '.'])
    return count

print count_safe_tiles(get_tiles(first_row, max_rows))
