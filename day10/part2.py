# -*- coding: utf-8 -*-

import sys

bots = {}
outputs = {}

def process(instructions):
    while instructions:
        for instruction in instructions[:]:
            if instruction.startswith('value'):
                details = instruction.split(' ')
                chip = int(details[1])
                bot = int(details[-1])
                if bot in bots:
                    bots[bot].append(chip)
                else:
                    bots[bot] = [chip]
                instructions.remove(instruction)
            elif instruction.startswith('bot'):
                details = instruction.split(' ')
                worker_bot = int(details[1])
                if worker_bot in bots and len(bots[worker_bot]) == 2:
                    low_chip = min(bots[worker_bot])
                    high_chip = max(bots[worker_bot])

                    low_container = bots if details[5] == 'bot' else outputs
                    low_key = int(details[6])
                    high_container = bots if details[10] == 'bot' else outputs
                    high_key = int(details[11])

                    if details[5] == 'bot' and len(low_container.get(low_key, [])) == 2:
                        continue
                    if details[10] == 'bot' and len(high_container.get(high_key, [])) == 2:
                        continue
                    
                    if low_key in low_container:
                        low_container[low_key].append(low_chip)
                    else:
                        low_container[low_key] = [low_chip]
                    if high_key in high_container:
                        high_container[high_key].append(high_chip)
                    else:
                        high_container[high_key] = [high_chip]
                    instructions.remove(instruction)

    return -1
                
instructions = sys.stdin.read().strip().split('\n')
print process(instructions)
print outputs[0][0] * outputs[1][0] * outputs[2][0]

