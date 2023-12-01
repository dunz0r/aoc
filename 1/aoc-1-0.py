#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Boilerplate for aoc
"""
import sys
import os
import re
sys.path.append(os.environ['AOCDIR'])
from aoc_utils import readInput as readInput, submitAnswer as submitAnswer

def main():
    singleNumberSearch = re.compile('[0-9]')

    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    numbers = []
    for line in input:
        firstHit = str(re.search(singleNumberSearch, line).group())
        # Reverse the line
        line = "".join(reversed(line))
        lastHit = str(re.search(singleNumberSearch, line).group())
        numbers.append(int(firstHit + lastHit))
    result = sum(numbers)
    print(result)
    #submitAnswer(result,2023,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
