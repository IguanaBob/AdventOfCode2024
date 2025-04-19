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
# Before coding: Try with lists of next stone.
#
# It's messy because it was a test that I abandoned part-way for other ideas.
#
###############################################################################

import sys

debug = True
debug2 = True
stones = []
blinks = 100
rainbow_stones = {}

class StoneList(list):
  def __setitem__(self, index, value):
    missing = index - len(self) + 1
    if missing > 0:
      self.extend([None] * missing)
    list.__setitem__(self, index, value)
  def __getitem__(self, index):
    try: return list.__getitem__(self, index)
    except IndexError: return None
                
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

def blinky(stone,stones,blink,max_blinks):
  while(blink < max_blinks):
    if(stone not in stones):
      if(stone == 0):
        nextStone = 1
        blinky(nextStone,stones,blink+1,max_blinks)
      elif ( len(str(stone)) % 2 == 0 ):
        half = len(str(stone)) / 2
        lefthalf = int(str(stone)[0:int(half)])
        righthalf = int(str(stone)[int(half):])
        nextStone = (lefthalf,righthalf)
        blinky(lefthalf,stones,blink+1,max_blinks)
        blinky(righthalf,stones,blink+1,max_blinks)
      else:
        nextStone = stone*2024
        blinky(nextStone,stones,blink+1,max_blinks)
      stones[stone] = nextStone
    else:
       nextStone = None
    return nextStone

def find_splits(stone,stones,blink,max_blinks,stones_dict,splits):
  print ("finding splits")
  while(blink < max_blinks):
    if(stone not in stones):
      stones[stone] = [ 0 ]
    if(len(stones[stone]) < max_blinks+1 and stone in stones_dict):
      if ( isinstance(stones_dict[stone],int) ):
        if (len(stones[stone]) < max_blinks+1 ): stones[stone].insert(blink,splits)
        find_splits(stones_dict[stone],stones,blink+1,max_blinks,stones_dict,splits)
      else:
        splits += 1
        if (len(stones[stone]) < max_blinks+1 ): stones[stone].insert(blink+1,splits)
        find_splits(stones_dict[stone][0],stones,blink+1,max_blinks,stones_dict,splits)
        find_splits(stones_dict[stone][1],stones,blink+1,max_blinks,stones_dict,splits)
      stones[stone].sort()
    return splits
  return splits
   

if __name__ == '__main__':

    stones = readfile()
    stonecount = 0
    resulting_stones = 0
    stones_dict = {}
    stone_splits = {}


    for stone in stones:
      blinky(stone,stones_dict,0,blinks)
      find_splits(stone,stone_splits,0,blinks,stones_dict,0)
      #print (stones_dict)

    #print (stones_dict)
    stone = 0
    
    
    #print (stones_dict)
    #print (stone_splits)
    print(stone_splits[0])
    print(stone_splits[1])
    print(stone_splits[2024])