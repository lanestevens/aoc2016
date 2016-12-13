# -*- mode: Python -*-

import hashlib

template = 'abbhdwsy{:d}'
#template = 'abc{:d}'
password = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
i = 0
while ' ' in password:
    this = template.format(i)
    hash = hashlib.md5(this).hexdigest()
    i += 1
    if hash.startswith('00000') and '0' <= hash[5] <= '7':
        j = int(hash[5])
        if password[j] == ' ':
            password[j] = hash[6]

print ''.join(password)
