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
    l = 0
    sum = 0
    red,blue,green = 12,13,14
    for game in input:

        index,game = game.split(": ")
        game = game.split(';')
        print(f'game {index}')
        red,blue,green = 12,13,14
        for pull in game[1].split(", "):
            if 'red' in pull:
                red -= int(red[0:1])
            if 'blue' in pull:
                blue -= int(blue[0:1])
            if 'green' in pull:
                green -= int(green[0:1])
        if not(red>=0 and b=>0 and c >=0):
            sum += int(index) + 1
            print(f'game {index} is possible, adding to sum. sum currently: {sum}')
            print(f' game_red: {game_red}, game_blue: {game_blue}, game_green: {game_green}')

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
