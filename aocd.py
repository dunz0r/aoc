#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Download puzzles for AOC
"""

import html2text
import argparse
import requests
import datetime
import shutil
import os

def main(args):
    curdate=datetime.datetime.now()
    if curdate.month != 12:
        print("Not december yet, specify year and day")
        exit(0)

    YEAR=0
    DAY=0
    if args.year:
        YEAR=args.year
    else:
        YEAR=curdate.year

    if args.day:
        DAY=args.day
    else:
        DAY=curdate.day

    SESSIONID=os.environ['AOCSESSION']
    DIR=os.environ['AOCDIR']
    PATH=os.environ['AOCDIR']+str(DAY)
    USER_AGENT="https://github.com/dunz0r/aoc2022, gf@hax0r.se"
    if args.secondpart:
        uri = 'http://adventofcode.com/{year}/day/{day}'.format(year=YEAR, day=DAY)
        response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
        description = response.text
        description = html2text.html2text(description)
        f = open(PATH+"/description", "w")
        f.write(description)
        f.close()
    if not os.path.exists(PATH):
        os.mkdir(PATH)
        uri = 'http://adventofcode.com/{year}/day/{day}/input'.format(year=YEAR, day=DAY)
        response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
        f = open(PATH+"/input", "w")
        f.write(response.text)
        f.close()
        uri = 'http://adventofcode.com/{year}/day/{day}'.format(year=YEAR, day=DAY)
        response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
        description = response.text
        description = html2text.html2text(description)
        f = open(PATH+"/description", "w")
        f.write(description)
        f.close()
        # Create boilerplate files
        filename = "{PATH}/aoc-{DAY}.py".format(PATH=PATH, DAY=DAY)
        shutil.copyfile("{dir}boilerplate.py".format(dir=DIR), filename)
        os.chmod(filename, 0o755)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Specify which day to download")
    parser.add_argument("-y", "--year", type=int, help="Specify which year to use")
    parser.add_argument("-2", "--secondpart", help="Download the second part of the challenge")
    args = parser.parse_args()
    main(args)
