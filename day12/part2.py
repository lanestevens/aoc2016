# -*- coding: utf-8 -*-

import re
import sys

a = 'a'
b = 'b'
c = 'c'
d = 'd'
registers = {a: 0, b: 0, c: 1, d: 0}

copyval = re.compile('cpy (?P<val>-*[0-9]+) (?P<dst>a|b|c|d)')
copyreg = re.compile('cpy (?P<src>a|b|c|d) (?P<dst>a|b|c|d)')
increg = re.compile('inc (?P<reg>a|b|c|d)')
decreg = re.compile('dec (?P<reg>a|b|c|d)')
jnzval = re.compile('jnz (?P<val>-*[0-9]+) (?P<steps>-*[0-9]+)')
jnzreg = re.compile('jnz (?P<reg>a|b|c|d) (?P<steps>-*[0-9]+)')
parsers = (copyval, copyreg, increg, decreg, jnzval, jnzreg)

def execute(instructions):
    ip = 0
    while ip < len(instructions):
        for parser in parsers:
            m = parser.match(instructions[ip])
            if m:
                this_parser = parser
                break

        if parser == copyval:
            registers[m.groupdict()['dst']] = int(m.groupdict()['val'])
        elif parser == copyreg:
            registers[m.groupdict()['dst']] = registers[m.groupdict()['src']]
        elif parser == increg:
            registers[m.groupdict()['reg']] += 1
        elif parser == decreg:
            registers[m.groupdict()['reg']] -= 1
        elif parser == jnzreg:
            if registers[m.groupdict()['reg']]:
                ip  += int(m.groupdict()['steps'])
                continue
        elif parser == jnzval:
            if int(m.groupdict()['val']):
                ip += int(m.groupdict()['steps'])
                continue
        else:
            raise ValueError('Unknown instruction:  {:s}'.format(instructions[ip]))
        ip += 1

instructions = sys.stdin.read().strip().split('\n')
execute(instructions)
print registers
