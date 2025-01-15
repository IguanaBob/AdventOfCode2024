#!/usr/bin/python3

###############################################################################
#
# 2024 Advent of Code, Day 02, Part 1
# Copyright © 2024,2025 Jonathan Hull
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU General Affero Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################
#
# ChatGPT's summary:
# The Red-Nosed Reindeer nuclear fusion plant needs help analyzing data 
# from reports that contain lists of numbers, called levels. A report is 
# considered safe if the levels are either all increasing or all decreasing, 
# and any two adjacent levels differ by at least 1 and at most 3. Your task 
# is to determine how many reports are safe based on these rules.
#
# My Reflection:
# The logic is similar to the original Bash version, but at least the file
# reading function is improved. It also moves the checking to it's own function
# rather than a loop inside main.
#
###############################################################################


def check_report():
    # Safety return values:
    #   0  = safe
    #   >0 = unsafe, any
    #   1  = unsafe, reason not provided
    #   2  = unsafe, equal levels
    #   3  = unsafe, direction change
    #   4  = unsafe, level change too large
    safety = 0  # Assume safe for now
    replen = len(report)
    direction = "?"
    if( int(report[0]) > int(report[1]) ):
        # Decreasing
        direction = ">"
    elif ( int(report[0]) < int(report[1]) ):
        # Increasing
        direction = "<"
    else:
        # Equal
        print("Unsafe! Levels 1 and 2 are equal")
        safety = 2
        return(safety)
    i = 0
    while ( i < (replen - 1) ):
        level = int(report[i])
        nextlevel = int(report[i+1])
        change = abs(level - nextlevel)
        if ( (( direction == ">" ) and ( level < nextlevel )) or (( direction == "<") and ( level > nextlevel ))):
            print("Unsafe! Direction change (" + str(nextlevel) + direction + str(level) + ")")
            safety = 3
            return(safety)
        elif( change > 3 ):
            print("Unsafe! Change greater than 3 (" + str(change) + ")")
            safety = 3
            return(safety)
        elif( change == 0 ):
            print("Unsafe! Level change is 0")
            safety = 2
            return(safety)
        i = i + 1
    safety = 0
    print("Safe!")
    return(safety)

# Begin main

numlines = 0
safereports = 0

with open('input', 'r') as file:
    for line in file:
        report = line.strip().split()
        numlines = numlines + 1
        print("Report: " + str(report))
        if(check_report() == 0):
            safereports = safereports + 1

# The answer, the total number of safe reports.
print("Safe reports: " + str(safereports))

exit(0)
