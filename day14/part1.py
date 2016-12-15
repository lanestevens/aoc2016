# -*- coding: utf-8 -*-

import hashlib
import re
import sys

def get_digest(salt, i):
    return hashlib.md5('{:s}{:d}'.format(salt, i)).hexdigest()

def has_companion(salt, start, c):
    s = re.compile('({:s})\\1{{4}}'.format(c))
    for i in range(start, start + 1000):
        m = s.search(get_digest(salt, i))
        if m:
            return True
    return False

def find_keys(salt):
    keys = []
    finder = re.compile('(.)\\1{2}')

    i = 0
    while True:
        m = finder.search(get_digest(salt, i))
        if m and has_companion(salt, i + 1, m.groups()[0]):
            keys.append(i)
            if len(keys) == 64:
                return i
        i += 1

print find_keys('cuanljph')

