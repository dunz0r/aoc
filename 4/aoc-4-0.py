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
    sum = 0
    for pair in input:
        first, second = pair.strip().split(',')
        first_start, first_end = map(int,first.split('-'))
        second_start, second_end = map(int,second.split('-'))
        if (first_start <= second_start <= first_end) or (
        first_start <= second_end <= first_end) or (
        second_start <= first_start <= second_end) or (
        second_start <= first_end <= second_end):
            sum += 1
    print(sum)
    #submitAnswer(result,2022,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
