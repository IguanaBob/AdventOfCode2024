#!/usr/bin/python3

###############################################################################
#
# 2024 Advent of Code, Day 02, Part 2
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
# The engineers introduce the Problem Dampener, which allows the reactor
# safety systems to tolerate a single bad level in a report. Now, the same
# rules apply, but if removing one level from an unsafe report makes it
# safe, the report counts as safe. Your task is to determine how many reports
# are now safe, considering this new tolerance for a single bad level.
#
# My Reflection:
# 130x faster than the Bash version due to reading the input from disk once.
#
###############################################################################

def check_report(rep):
    print("Checking report: " + str(rep))

    # Safety return values:
    #   0  = safe
    #   >0 = unsafe, any
    #   1  = unsafe, reason not provided
    #   2  = unsafe, equal levels
    #   3  = unsafe, direction change
    #   4  = unsafe, level change too large
    safety = 0  # Assume safe for now

    replen = len(rep)

    direction = "?"
    if( int(rep[0]) > int(rep[1]) ):
        # Decreasing
        direction = ">"
    elif ( int(rep[0]) < int(rep[1]) ):
        # Increasing
        direction = "<"
    else:
        # Equal
        print("Unsafe! Levels 1 and 2 are equal")
        safety = 2
        return(safety)

    i = 0
    while ( i < (replen - 1) ):
        level = int(rep[i])
        nextlevel = int(rep[i+1])
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

def check_dampened(raw_rep):
    replen = len(raw_rep)
    print("Dampening...")
    i = 0
    while(i < ( replen ) ):
        print("Removing level #" + str(i+1))
        damp_rep = raw_rep.copy()
        # Popping from a list is so much cleaner than the Bash nonesense in the original.
        damp_rep.pop(i)
        safety = check_report(damp_rep)
        if(safety == 0):
            return(safety)
        i = i + 1
    return(safety)

# Begin main

numlines = 0
safereports = 0

with open('input', 'r') as file:
    for line in file:
        report = line.strip().split()
        numlines = numlines + 1
        print("Report: " + str(report))
        if(check_report(report) != 0):
            if(check_dampened(report) == 0):
                safereports = safereports + 1
        else:
            safereports = safereports + 1

# The answer, the total number of safe reports after dampening
print("Safe reports: " + str(safereports))

exit(0)
