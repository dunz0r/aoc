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
A, X = Rock, 0
B, Y = Paper, 1
C, Z = Scissors, 2

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
    games = []
    score = 0
    for line in input:
        line = line.split(" ")
        games.append([translate_move(line[0]), translate_move(line[1])])
    for game in games:
        if game[1] == 0:
            print("loose")
            if game[0] == 0:
                game[1] = 2
            elif game[0] == 1:
                game[1] = 0
            elif game[0] == 2:
                game[1] = 1
        elif game[1] == 1:
            print("draw")
            game[1] = game[0]
        elif game[1] == 2:
            print("win")
            if game[0] == 0:
                game[1] = 1
            elif game[0] == 1:
                game[1] = 2
            elif game[0] == 2:
                game[1] = 0
        winner = scoring_table[game[0]][game[1]]
        if game[1] == game[0]:
            score = score + 3 + (game[1]+1)
        elif winner == game[1]:
            score = score +6 + (game[1]+1)
        elif winner == game[0]:
            score = score + (game[1] + 1)
        print("Game input: {inp}, score: {p}".format(inp=game, p=score))
    print(score)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
