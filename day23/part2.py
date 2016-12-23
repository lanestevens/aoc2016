# -*- coding: utf-8 -*-

import re
import sys

a = 'a'
b = 'b'
c = 'c'
d = 'd'
registers = {a: 12, b: 0, c: 0, d: 0}

copyval = re.compile('cpy (?P<val>-*[0-9]+) (?P<dst>a|b|c|d)')
copyreg = re.compile('cpy (?P<src>a|b|c|d) (?P<dst>a|b|c|d)')
increg = re.compile('inc (?P<reg>a|b|c|d)')
decreg = re.compile('dec (?P<reg>a|b|c|d)')
jnz = re.compile('jnz (?P<v1>[^ ]+) (?P<v2>[^ ]+)')
tgl = re.compile('tgl (?P<reg>a|b|c|d)')
parsers = (copyval, copyreg, increg, decreg, jnz, tgl)

def toggle(instruction):
    for parser in parsers:
        m = parser.match(instruction)
        if m:
            this_parser = parser
            break

    if parser == copyval:
        return instruction.replace('cpy', 'jnz')
    if parser == copyreg:
        return instruction.replace('cpy', 'jnz')
    if parser == increg:
        return instruction.replace('inc', 'dec')
    if parser == decreg:
        return instruction.replace('dec', 'inc')
    if parser == jnz:
        return instruction.replace('jnz', 'cpy')
    if parser == tgl:
        return instruction.replace('tgl', 'inc')
    
def execute(instructions):
    ip = 0
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
        elif this_parser == tgl:
            tgl_ip = ip + registers[m.groupdict()['reg']]
            if 0 <= tgl_ip < len(instructions):
                instructions[tgl_ip] = toggle(instructions[tgl_ip])
        else:
            raise ValueError('Unknown instruction:  {:s}'.format(instructions[ip]))
        ip += 1

instructions = sys.stdin.read().strip().split('\n')
execute(instructions)
print registers
