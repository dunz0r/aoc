#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Share utilities for aoc
"""
import requests
import html2text
import os


def readInput():
    f = open("input", "r")
    return f.readlines()

def submitAnswer(input, year, day, level):
    SESSIONID=os.environ['AOCSESSION']
    uri = 'http://adventofcode.com/{y}/day/{d}/answer'.format(y=year, d=day)
    answer = requests.post(uri, cookies={'session': SESSIONID}, data={'answer':str(input), 'level':str(level)}, headers={'User-Agent':'https://github.com/dunz0r/aoc2022, gf@hax0r.se'})
    return html2text.html2text(answer.text)
