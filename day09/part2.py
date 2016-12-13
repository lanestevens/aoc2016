# -*- coding: utf-8 -*-

import sys

def decompressed_length(compressed):
    if compressed == '':
        return 0

    if compressed[0] == '(':
        control_end = compressed.find(')')
        control = compressed[1:control_end]
        compressed = compressed[control_end + 1:]
        chars, repeats = [int(x) for x in control.split('x')]
        data = compressed[:chars]
        compressed = compressed[chars:]
        return repeats * decompressed_length(data) + decompressed_length(compressed)

    return 1 + decompressed_length(compressed[1:])


# test_data = [('(3x3)XYZ', 9),
#              ('X(8x2)(3x3)ABCY', 20),
#              ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
#              ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
#              ]
# for compressed, expected_length in test_data:
#     actual_length = decompressed_length(compressed)
#     print compressed, expected_length, actual_length, expected_length == actual_length

print decompressed_length(sys.stdin.read())
