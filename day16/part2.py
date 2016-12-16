# -*- coding: utf-8 -*-

the_seed = '10000'
the_limit = 20

the_seed = '01110110101001000'
the_limit = 35651584

def dragon(seed, limit):
    if len(seed) >= limit:
        return seed[:limit]

    return dragon(seed + '0' + ''.join(['1' if x == '0' else '0' for x in reversed(seed)]), limit)

def chksum(data):
    c = data
    buf = bytearray(' '* ((len(c) /2)  + 1))
    while (len(c) % 2) == 0:
        data = c
        i = 0
        j = 0
        while i < len(data):
            buf[j] = '1' if data[i] == data[i + 1] else '0'
            i += 2
            j += 1
        c = str(buf[:j])

    return c

data = dragon(the_seed, the_limit)
c = chksum(data)
while (len(c) % 2) == 0:
    c = chksum(c)
print c
