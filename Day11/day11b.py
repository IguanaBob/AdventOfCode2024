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
#
# During: ...for 4 hours (34 blinks in)... (cancels and changes to storing as
# int instead of str) ...and wait...
#
# 46 minutes later: Canceled. Still too slow, but it used less memory.
#
# Rethink... Fork? Store values for lookup? Iterate once but repeat at each
# stone then pop off?
# Forking will give it a speedup, but the slowness is due to the exponential
# growth so it may not be enough. Calculating once and storing the count in
# a dictionary won't be too useful as it's unlikely we will see many repeats.
# Iterating once will just change the order, likely won't help much. I am going
# to have to do some testing.
# 
# Trying forking: Got it working with multiprocessing. Still takes forever.
# Going to let it run overnight.
# While that runs, I'm going to test store/lookup rainbow tables to test for
# repetition that can be eliminated. That will be in day11b_rainbow.py
#
# See day11b_final.py for information on the final solution.
#
###############################################################################

import sys
import multiprocessing
import os

debug = False
debug2 = True
stones = []
blinks = 75
forks = 8
blinks_before_forking = 13
global stonecount
stonecount = 0

def readfile():
    if 'stonecount' not in vars() and 'stonecount' not in globals():
        global stonecount
        stonecount = 0
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
        stonecount += 1
    return stones

def blink(stones):
    global stonecount
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
    return len(stones)

def blink_multi(stones,blinks):
    i = 0
    while ( i < blinks ):
        blink(stones)
        i += 1
    return len(stones)

if __name__ == '__main__':

    stones = readfile()
    k = 0
    if (blinks_before_forking > blinks): blinks_before_forking = blinks
    while k < blinks_before_forking:
        blink(stones)
        k += 1
    stonecount = 0
    print("Begining forking...")
    with multiprocessing.Pool(processes=forks) as pool:
       results = pool.starmap(blink_multi, [([sl],blinks-blinks_before_forking) for sl in stones])
       #print("results: " + str(results))
       stonecount = sum(results)

    print("Stones after " + str(blinks) + " blinks: " + str(stonecount))
