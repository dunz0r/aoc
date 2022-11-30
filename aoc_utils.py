#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Share utilities for aoc
"""
import requests
import html2text
import os

DIR=os.environ['AOCDIR']
PATH=os.environ['AOCDIR']+'./'+str(DAY)

def readInput():
    f = open(PATH+"/input", "r")
    return f.readlines()

def submitAnswer(input,year, day, level):
    SESSIONID=os.environ['AOCSESSION']
    uri = 'http://adventofcode.com/{year}/day/{day}/answer'.format(year, day)
    answer = requests.post(uri, cookies={'session': SESSIONID}, data={'answer':str(input), 'level':str(level)})
    return html2text.html2text(answer.text)
