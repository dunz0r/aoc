#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Boilerplate for aoc
"""
import datetime
import requests
import html2text
import os

curdate=datetime.datetime.now()
YEAR=curdate.year
DAY=curdate.day
DIR=os.environ['AOCDIR']
PATH=os.environ['AOCDIR']+'./'+str(DAY)

def readInput():
    f = open(PATH+"/input", "r")
    return f.readlines()

def submitAnswer(input,level):
    SESSIONID=os.environ['AOCSESSION']
    uri = 'http://adventofcode.com/{year}/day/{day}/answer'.format(year=YEAR, day=DAY)
    answer = requests.post(uri, cookies={'session': SESSIONID}, data={'answer':str(input), 'level':str(level)})
    return html2text.html2text(answer.text)

def main():
    input = readInput()
    result = '.'.join(input)
    submitAnswer(result,1)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
