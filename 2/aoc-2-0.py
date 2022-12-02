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

"""
Scoring
A, X = Rock
B, Y = Paper
C, Z = Scissors

Rock > Scissors
Paper > Rock
Scissors > Paper
"""

def translate_move(move):
    game_map = {
            'A': 0,
            'X': 0,
            'B': 1,
            'Y': 1,
            'C': 2,
            'Z': 2,
        }
    return game_map.get(move)

def main():
    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    scoring_table = [[-1,1,0], [1,-1,2], [0,2,-1]]
    split_input = []
    score = 0
    for line in input:
        split = line.split(" ")
        split_input.append(line.split(" "))
    for game in split_input:
        result = scoring_table[translate_move(game[0])][translate_move(game[1])]
        print(result)
        score += result
    print(score)
    submitAnswer(score,2022,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
