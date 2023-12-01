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

def toNumber(input):
    if input.isdigit():
        print(input)
        return int(input)
    else:
        numberMap = { 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                     'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}
        print(input, numberMap[input])
        return int(numberMap[input])

def main():
    singleNumberSearch = re.compile(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))')

    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    numbers = []
    for line in input:
        print(line)
        hits = re.findall(singleNumberSearch, line)
        firstHit = toNumber(hits[0])
        lastHit = toNumber(hits[-1])
        print(str(firstHit)+str(lastHit))
        numbers.append(int(str(firstHit)+str(lastHit)))
    result = sum(numbers)
    print(result)
    #submitAnswer(result,2023,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
