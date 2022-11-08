#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2022 gabfor@corp.unibap.net <gabfor@corp.unibap.net@BAP024L>
#
# Distributed under terms of the MIT license.

"""
Download todays puzzle for AOC
"""

import requests
import datetime
import os
import html2text

def main():
    curdate=datetime.datetime.now()
    YEAR=curdate.year
    DAY=curdate.day
    SESSIONID=os.environ['AOCSESSION']
    USER_AGENT="Sneaky Pete"
    PATH='./'+str(DAY)
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
        print(description)
        f = open(PATH+"/description", "w")
        f.write(description)
        f.close()
        

if __name__ == "__main__":
    main()
