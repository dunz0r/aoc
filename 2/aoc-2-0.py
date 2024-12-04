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

def is_safe_report(report):
    """
    Levels are safe if any of the conditions below are true:
        The levels are either all increasing or all decreasing.
        Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if any(abs(diff) < 1 or abs(diff) > 3 for diff in differences):
        return False
    
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True
    
    return False

def count_safe_reports(reports):
    """
    Counts the number of safe reports in the given list of reports.
    """
    return sum(is_safe_report(report) for report in reports)

def main():
    input = readInput()
    input = list(map(lambda x:x.strip(),input))
    inputInt = []
    for data in input:
        splData = data.split(' ')
        splData = [int (x) for x in splData]
        inputInt.append(splData)
    safeCount = count_safe_reports(inputInt)
    print(f"Number of safe reports: {safeCount}")

if __name__ == "__main__":
    if not 'AOCSESSION' in os.environ or not 'AOCDIR' in os.environ:
        print("Set your variables")
        exit(1)
    main()
