#! /usr/bin/env python3
# vim:fenc=utf-8
#

"""
Download todays puzzle for AOC
"""

import html2text
import requests
import datetime
import os
import shutil

def main():
    curdate=datetime.datetime.now()
    YEAR=curdate.year
    YEAR=2021
    DAY=curdate.day
    DAY=3
    SESSIONID=os.environ['AOCSESSION']
    DIR=os.environ['AOCDIR']
    PATH=os.environ['AOCDIR']+str(DAY)
    USER_AGENT="dunz0rs downloading script"
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
        for i in range(2):
            filename = "{PATH}/aoc-{DAY}-{number}.py".format(number=i, PATH=PATH, DAY=DAY)
            shutil.copyfile("{dir}boilerplate.py".format(dir=DIR), filename)

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
