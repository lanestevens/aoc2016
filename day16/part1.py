# -*- coding: utf-8 -*-

the_seed = '10000'
the_limit = 20

the_seed = '01110110101001000'
the_limit = 272

def dragon(seed, limit):
    if len(seed) >= limit:
        return seed[:limit]

    return dragon(seed + '0' + ''.join(['1' if x == '0' else '0' for x in reversed(seed)]), limit)

def chksum(data):
    if data:
        return ('1' if data[0] == data[1] else '0') + chksum(data[2:])
    return ''

data = dragon(the_seed, the_limit)
c = chksum(data)
while (len(c) % 2) == 0:
    c = chksum(c)
print c
