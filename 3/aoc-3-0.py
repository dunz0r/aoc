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

def main():
    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    for index, line in enumerate(input):
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        input[index] = [firstpart, secondpart]
    #submitAnswer(result,2022,1,1)
    total = 0
    for rucksack in input:
        in_both = [ c for c in rucksack[0] if c in rucksack[1]]
        if not in_both: continue
        item = in_both[0]
        total += ord(item) - 96 if item.islower() else ord(item) - 65 + 27
    print(total)
    #submitAnswer(result,2022,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
