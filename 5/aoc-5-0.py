#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Boilerplate for aoc
"""
import sys
import os
import re
import textwrap
sys.path.append(os.environ['AOCDIR'])
from aoc_utils import readInput as readInput, submitAnswer as submitAnswer

def main():
    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    container_stack = []
    for line in input:
        if re.match('^\[.*$',line):
                container_stack.append([line[i:i+4] for i in range(0, len(line), 4)])
        else:
            break

    for stack in container_stack:
        print(stack)
    #submitAnswer(result,2022,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
