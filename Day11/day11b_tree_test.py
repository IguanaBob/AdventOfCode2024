



#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 11, Part 2, Rainbow lookup version
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
# Before coding: I haven't gotten back to the parallel idea since my initial
# test seeing my laptop still wasn't fast enough, which I figured would be
# the case.
# Decided to try expermimenting with a tree. Digging deep into my 20+ year old
# memories from college for this one while also researching how to do a tree in
# python.
#
# It's messy because it was a test that I abandoned part-way for other ideas.
#
###############################################################################

import sys

debug = True
debug2 = True
stones = []
blinks = 6
rainbow_stones = {}

class Stone:
    def __init__(self, number):
        self.nextStone = None
        self.newStone = None
        self.number = number
    def findNextStone(self):
        if (self.number == 0):
            # Rule 1: 0 becomes 1
            self.nextStone = Stone(1)
        elif ( len(str(self.number)) % 2 == 0 ):
            # Rule 2: Even number of digits splits.
            half = len(str(self.number)) / 2
            lefthalf = int(str(self.number)[0:int(half)])
            righthalf = int(str(self.number)[int(half):])
            self.nextStone = Stone(lefthalf)
            self.newStone = Stone(righthalf)
        else:
            # Rule 3, default: Multiply by 2024
            self.nextStone = Stone(self.number * 2024)

                
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
    # convert to int for less memory usage and faster processing
    i = 0
    while ( i < len(stones) ):
        stones[i] = int(stones[i])
        i += 1
        stonecount += 1
    return stones

def rainbow_blink_build(stone,start_stone,blink_max,blink_count=0):
    if blink_count <= blink_max:
        if ( stone not in rainbow_stones or len(rainbow_stones[start_stone]) <= blink_count ):
            if ( stone == 0 ):
                # Rule 1
                newstone = 1
                splits = False
                print("Storing rainbow_stones[" + str(stone) + "][" + str(blink_count) + "] = " + str(splits) )
                rainbow_stones[start_stone] = {}
                rainbow_stones[start_stone][blink_count] = splits
                if ( blink_count < blink_max ): rainbow_blink_build(newstone,start_stone,blink_max,blink_count+1)
            elif ( len(str(stone)) % 2 == 0 ):
                # Rule 2
                splits = True
                half = len(str(stone)) / 2
                lefthalf = int(str(stone)[0:int(half)])
                righthalf = int(str(stone)[int(half):])
                print("Storing rainbow_stones[" + str(start_stone) + "][" + str(blink_count) + "] = " + str(splits) )
                rainbow_stones[start_stone] = {}
                rainbow_stones[start_stone][blink_count] = splits
                if ( blink_count < blink_max ):
                    rainbow_blink_build(lefthalf,lefthalf,blink_max-blink_count-1,0)
                    rainbow_blink_build(righthalf,righthalf,blink_max-blink_count-1,0)
            else:
                # Rule 3, default
                splits = False
                newstone = stone * 2024
                print("Storing rainbow_stones[" + str(start_stone) + "][" + str(blink_count) + "] = " + str(splits) )
                rainbow_stones[start_stone] = {}
                rainbow_stones[start_stone][blink_count] = splits
                if ( blink_count < blink_max ): rainbow_blink_build(newstone,start_stone,blink_max,blink_count+1)



# Funny name, serious sandwi... uh... function.
# It will calculate the number of stones that result from an initial stone
# and a specified number of blinks, storing it in a dictionary for later lookup.
def blinky(stone,start_stone,blink_max,start_stone_count,blink_num=0):
    stonecount = 0
    # Initialize entries in the table
    if ( stone not in rainbow_stones ): rainbow_stones[stone] = {}
    if ( start_stone not in rainbow_stones ): rainbow_stones[start_stone] = {}
    if ( len(rainbow_stones[stone]) == 0 ): rainbow_stones[stone][0] = 1

    if ( blink_num >= blink_max - 1): return stonecount

    # Rule 1
    if ( stone == 0 ):
        if ( len(rainbow_stones[start_stone]) <= blink_num ): rainbow_stones[start_stone][blink_num] = start_stone_count
        if ( blink_num < blink_max - 1 ):
            newstone = 1
            stonecount = blinky(newstone,start_stone,blink_max,start_stone_count,blink_num+1)
    #        return stonecount
        else:
            stonecount = 1
   #         return stonecount
    # Rule 2
    elif ( len(str(stone)) % 2 == 0 ):
        if ( len(rainbow_stones[start_stone]) <= blink_num ): rainbow_stones[start_stone][blink_num] = start_stone_count + 1
        if ( blink_num < blink_max ):
            half = len(str(stone)) / 2
            lefthalf = int(str(stone)[0:int(half)])
            righthalf = int(str(stone)[int(half):])
            stonecount = ( blinky(lefthalf,start_stone,blink_max,start_stone_count,blink_num+1) + blinky(righthalf,start_stone,blink_max,start_stone_count,blink_num+1) )
  #          return stonecount
        else:
            stonecount = 2
 #           return stonecount
        #left/right nonesense with two recursive calls if blinks > 1
    # Rule 3, default
    else:
        if ( len(rainbow_stones[start_stone]) <= blink_num ): rainbow_stones[start_stone][blink_num] = start_stone_count
        if ( blink_num < blink_max ):
            newstone = stone * 2024
            stonecount = blinky(newstone,start_stone,blink_max,start_stone_count,blink_num+1)
#            return stonecount
        else:
            stonecount = 1
#            return stonecount
    if debug: print("Stone: " + str(stone) + " Blinks: " + str(blink_max - blink_num) + " Result: " + str(stonecount))
    if debug: print("Starting stone: " + str(start_stone) + " Blinks: " + str(blink_num) + " Result: " + str(stonecount))
    return stonecount

if __name__ == '__main__':

    stones = readfile()
    stonecount = 0
    resulting_stones = 0
#    for stone in stones:
#        stonecount += blinky(stone,stone,blinks,1)
#        #rainbow_blink_build(stone,stone,blinks)
#    if debug: print(stonecount)
#    if debug: print(rainbow_stones)
#
#    print("Stones after " + str(blinks) + " blinks: " + str(resulting_stones))

root = Stone(40)
root.findNextStone()
print (root.number)
print (root.nextStone.number)
print (root.newStone.number)