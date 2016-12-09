# -*- coding: utf-8 -*-

import sys

def decompress(compressed):
    decompressed = ''
    while compressed:
        if compressed[0] == '(':
            control_end = compressed.find(')')
            control = compressed[1:control_end]
            compressed = compressed[control_end + 1:]
            chars, repeats = [int(x) for x in control.split('x')]
            data = compressed[:chars]
            compressed = compressed[chars:]
            decompressed += data * repeats
        else:
            decompressed +=compressed[0]
            compressed = compressed[1:]

    return decompressed

# test_data = [('ADVENT', 'ADVENT'),
#              ('A(1x5)BC', 'ABBBBBC'),
#              ('(3x3)XYZ', 'XYZXYZXYZ'),
#              ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG'),
#              ('(6x1)(1x3)A', '(1x3)A'),
#              ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY'),
#              ]
# for compressed, decompressed in test_data:
#     actual = decompress(compressed)
#     print compressed, decompressed, actual, decompressed == actual

print len(decompress(sys.stdin.read()))
