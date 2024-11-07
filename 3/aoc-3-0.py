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
    for rindex,row in enumerate(input):
        print(row)
        for cindex,col in enumerate(row):
            if col is not '.':
                print(col)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
