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
    """
    Levels are safe if any of the conditions below are true:
        The levels are either all increasing or all decreasing.
        Any two adjacent levels differ by at least 1 and at most 3.
    """
    tally = 0
    inputInt = []
    for idx,data in enumerate(input):
        splData = data.split(' ')
        splData = [int (x) for x in splData]
        inputInt.append(splData)
    for ix, x in enumerate(inputInt):
        print(x)
        if x[ix] <= (x[ix + 3]):
             print("Safe")

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
