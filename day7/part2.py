# -*- coding: utf-8 -*-

import re
import sys

def get_abas(l):
    abas = []
    for segment in l:
        for i in range(len(segment) - 2):
            if segment[i] == segment[i + 2] and segment[i] != segment[i + 1]:
                abas.append(segment[i:i + 3])
    return abas

def get_babs(abas):
    babs = []
    for aba in abas:
        babs.append(aba[1] + aba[0] + aba[1])

    return babs

def valid_ssl(ip):
    segments = re.findall('([a-z]+)', ip)
    outs = [segments[x] for x in range(0, len(segments) + 1, 2)]
    ins = [segments[x] for x in range(1, len(segments), 2)]

    abas = get_abas(outs)
    babs = get_babs(abas)
    for bab in babs:
        for this_in in ins:
            if bab in this_in:
                return True

    return False

count = 0
for line in sys.stdin.readlines():
    line = line.strip()
    if valid_ssl(line):
        count += 1

print count

    
