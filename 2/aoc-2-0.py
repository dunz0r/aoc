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
    max_red = 12
    max_green = 13
    max_blue = 14
    possible_games = []
    games = []
    for game in input:
        max_counts = {}
        game_id, pulls = game.split(": ")
        game_id = game_id.replace('Game ', '')
        pulls = pulls.split("; ")
        for pull in pulls:
            for cubeset in pull.split(', '):
                count, colour = cubeset.split(' ')
                count = int(count)

                if colour not in max_counts or count > max_counts[colour]:
                    max_counts[colour] = count

            games.append({
                'id': int(game_id),
                'max_counts': max_counts
                })

    for game in games:
        if game['max_counts'].get('red', 0) > max_red:
            continue

        if game['max_counts'].get('blue', 0) > max_blue:
            continue

        if game['max_counts'].get('green', 0) > max_green:
            continue

        print(game['id'])
        possible_games.append(game['id'])
    print(sum(possible_games))


                
    #submitAnswer(result,2022,1,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
