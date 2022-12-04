#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Boilerplate for aoc
"""
import sys
import os
sys.path.append(os.environ['AOCDIR'])
from aoc_utils import readInput as readInput, submitAnswer as submitAnswer

def to_priority(item):
        return ord(item) - 96 if item.islower() else ord(item) - 65 + 27

def main():
    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    #submitAnswer(result,2022,1,1)
    sum = 0
    rucksack_groups = []
    for i in range(0, len(input), 3):
        rucksack_groups.append(input[i:i + 3])
    for group in rucksack_groups:
        badge = ''.join(set(group[0]).intersection(*group[1:]))
        print(badge)
        sum += to_priority(str(badge))
    print(sum)


    #submitAnswer(result,2022,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
