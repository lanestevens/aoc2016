# -*- coding: utf-8 -*-

import re
import sys

a = 'a'
b = 'b'
c = 'c'
d = 'd'
registers = {a: 9, b: 0, c: 0, d: 0}

copyval = re.compile('cpy (?P<val>-*[0-9]+) (?P<dst>a|b|c|d)')
copyreg = re.compile('cpy (?P<src>a|b|c|d) (?P<dst>a|b|c|d)')
increg = re.compile('inc (?P<reg>a|b|c|d)')
decreg = re.compile('dec (?P<reg>a|b|c|d)')
jnz = re.compile('jnz (?P<v1>[^ ]+) (?P<v2>[^ ]+)')
out = re.compile('out (?P<v>[^ ]+)')
parsers = (copyval, copyreg, increg, decreg, jnz, out)

def execute(instructions):
    ip = 0
    out_vals = []
    while ip < len(instructions):
        this_parser = None
        for parser in parsers:
            m = parser.match(instructions[ip])
            if m:
                this_parser = parser
                break

        if this_parser == copyval:
            registers[m.groupdict()['dst']] = int(m.groupdict()['val'])
        elif this_parser == copyreg:
            registers[m.groupdict()['dst']] = registers[m.groupdict()['src']]
        elif this_parser == increg:
            registers[m.groupdict()['reg']] += 1
        elif this_parser == decreg:
            registers[m.groupdict()['reg']] -= 1
        elif this_parser == jnz:
            try:
                v1 = int(m.groupdict()['v1'])
            except:
                v1 = registers[m.groupdict()['v1']]

            try:
                v2 = int(m.groupdict()['v2'])
            except:
                v2 = registers[m.groupdict()['v2']]
                
            if v1:
                ip += v2
                continue
        elif this_parser == out:
            try:
                v = int(m.groupdict()['v'])
            except:
                v = registers[m.groupdict()['v']]
            if v in (0, 1):
                out_vals.append(v)
                for i in range(len(out_vals)):
                    if (i % 2) != out_vals[i]:
                        return False
                if len(out_vals) >= 20:
                    return True
            else:
                return False
        else:
            raise ValueError('Unknown instruction:  {:s}'.format(instructions[ip]))
        ip += 1

instructions = sys.stdin.read().strip().split('\n')
start_a = 1
while True:
    registers = {a: start_a, b: 0, c: 0, d: 0}
    if execute(instructions):
        print start_a
        break
    print '{:d} failed'.format(start_a)
    start_a += 1
