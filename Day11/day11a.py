#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 11, Part 1
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
# ChatGPT's summary: The Plutonian Pebbles change with each blink following
# specific rules: a stone marked 0 becomes 1; if a stone's number has an even
# number of digits, it splits into two stones with the left half on the left
# and the right half on the right; otherwise, a stone is replaced by one
# engraved with its number multiplied by 2024. The order of stones remains
# preserved, and your task is to determine how many stones there will be after
# blinking 25 times.
#
# My Reflection:
# After reading description: Well, seems like just more array manipulation, and
# probably easier than some of the previous days. No sweat.
#
###############################################################################

import sys
import re

debug = False
stones = []

def readfile():
    if (len(sys.argv) > 1):
        inputfile = sys.argv[1]
    else:
        inputfile = "input"

    with open(inputfile,"r") as file:
        if debug: print("Reading input...")
        with open(inputfile,"r") as file:
            for row in file:
                stones.append(row.strip())
    return stones

def printmap(stones):
    for row in stones:
        print("".join(row))
    return

def blink(stones):
    pos = 0
    while ( pos < len(stones) - 1 ):
        print( "Checking pos " + str(pos) + ": " + stones[pos] )
        if ( stones[pos] == "0" ):
            # Rule 1: If stone is 0, replaced with 1.
            stones[pos] = "1"
        elif ( len(stones[pos]) % 2 == 0 ):
            # Rule 2: If stone is even number of digits, replaced by 2 stones. Left stone has left half of digits, right stone has right half of digits, drop leading zeros.
            half = len(stones[pos])/2
            leftnum = stones[pos][0:half-1]
            rightnum = stones[pos][half:]
            stones[pos] = leftnum
            pos += 1
            stones.insert(pos,rightnum)
        else:
            # Rule 3: Default: Stone replaced by stone with old stone's number * 2024.
            stones[pos] = str( int(stones[pos]) * 2024 )
    pos += 1
    return stones

stones = readfile()
printmap(stones)
blink(stones)
printmap(stones)
#print(score)
