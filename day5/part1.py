# -*- mode: Python -*-

import hashlib

password = ''
i = 0
template = 'abbhdwsy{:d}'
#template = 'abc{:d}'
while len(password) != 8:
    this = template.format(i)
    hash = hashlib.md5(this).hexdigest()
    i += 1
    if hash.startswith('00000'):
        password += hash[5]

print password
