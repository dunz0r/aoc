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
    tmpinput = readInput()
    input = []
    elfs_calories = []
    for i in range(len(tmpinput)):
        input.append(tmpinput[i].strip('\n'))
    current_calories=0
    elf = 0
    for line in input:
        if line == "":
            elf += 1
            print(str(current_calories)+"\nelf"+str(elf))
            elfs_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories = current_calories + int(line)
    elfs_calories.sort()
    print(elfs_calories[-1])

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
