#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 11, Part 2
# Copyright © 2025 Jonathan Hull
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
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>. 
#
###############################################################################
#
# ChatGPT's summary:
# (I didn't include because the only difference is the blink count is now 75)
#
# My Reflection:
# After reading description: Okay, so I change blinks to 75 and wait...
# During: ...for 4 hours (34 blinks in)... (cancels and changes to storing as
# int instead of str) ...and wait...
# 
#
# There may be a faster way, possibly iterating once only but moving backwards
# after a change, so I may revisit later to try it for fun.
#
###############################################################################

import sys

debug = False
debug2 = True
stones = []
blinks = 75

def readfile():
    if (len(sys.argv) > 1):
        inputfile = sys.argv[1]
    else:
        inputfile = "input"

    with open(inputfile,"r") as file:
        if debug: print("Reading input...")
        stones = file.readline().strip().split(" ")

    i = 0
    while ( i < len(stones) ):
        stones[i] = int(stones[i])
        i += 1
    return stones

#def printstones(stones):
#    print(" ".join(stones))
#    return

def blink(stones):
    pos = 0
    while ( pos < len(stones) ):
        if debug: print( "Checking pos " + str(pos) + ": " + str(stones[pos]) )
        if ( stones[pos] == 0 ):
            # Rule 1: If stone is 0, replaced with 1.
            if debug: print("Found 0, changing to 1")
            stones[pos] = 1
        elif ( len(str(stones[pos])) % 2 == 0 ):
            # Rule 2: If stone is even number of digits, replaced by 2 stones. Left stone has left half of digits, right stone has right half of digits, drop leading zeros.
            half = len(str(stones[pos]))/2
            leftnum = str(stones[pos])[0:int(half)]
            # Casting to int temporarily is the easiest way to remove leading zeros
            rightnum = str(int(str(stones[pos])[int(half):]))
            if debug: print("Found even number of digits, splitting stone: " + leftnum + " " + rightnum)
            stones[pos] = int(leftnum)
            pos += 1
            stones.insert(pos,int(rightnum))
        else:
            # Rule 3: Default: Stone replaced by stone with old stone's number * 2024.
            if debug: print("Default rule, multiplying by 2024: " + str(int(stones[pos]) * 2024))
            stones[pos] = stones[pos] * 2024
        pos += 1
    return stones

stones = readfile()
#printstones(stones)
i = 0
while ( i < blinks ):
    blink(stones)
#    if debug: printstones(stones)
    i += 1
    if debug2: print("Blinks: " + str(i))
    if debug2: print("Stones: " + str(len(stones)))
print("Stones after " + str(blinks) + " blinks: " + str(len(stones)))
