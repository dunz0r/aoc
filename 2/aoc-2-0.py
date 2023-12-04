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
    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    sum = 0
    for index, game in enumerate(input):
        game = re.sub('^Game \d{,3}: ','', game)
        game = game.split(';')
        print(f'game {index}')
        game_red = 0
        game_blue = 0
        game_green = 0
        for pull in game:
            red = re.search('[0-9]{,2} red', pull)
            if red:
                game_red += int(red[0][0:1])
            if not red:
                blue = 0
            blue = re.search('[0-9]{,2} blue', pull)
            if blue:
                game_blue += int(blue[0][0:1])
            if not blue:
                blue = 0
            green = re.search('[0-9]{,2} green', pull)
            if green:
                game_green += int(green[0][0:1])
            if not green:
                green = 0
        if game_red <= 12 and game_green <= 13 and game_blue <= 14:
            sum += index +1
            print(f'Game {index} is possible, adding to sum. Sum currently: {sum}')
            print(f' game_red: {game_red}, game_blue: {game_blue}, game_green: {game_green}')

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
