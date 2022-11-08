#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Boilerplate for aoc
"""
import os
from ..aoc_utils import readInput as readInput, submitAnswer as submitAnswer

def main():
    input = readInput()
    result = '.'.join(input)
    submitAnswer(result,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
