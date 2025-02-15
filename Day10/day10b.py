#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 10, Part 2
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
#
# My Reflection:
# Easiest part-2 ever. I just uncommented the visited.append() lines so it
# would check multiple routes.
#
###############################################################################

import sys
import re

debug = False
topomap = []

def readfile():
    if (len(sys.argv) > 1):
        inputfile = sys.argv[1]
    else:
        inputfile = "input"

    with open(inputfile,"r") as file:
        if debug: print("Reading input...")
        with open(inputfile,"r") as file:
            for row in file:
                topomap.append(row.strip())
    return tuple(topomap)

def printmap(topomap):
    for row in topomap:
        print("".join(row))
    return

def findtrailheads(topomap):
    if debug: print("Finding trailheads...")
    rownum = 0
    trailheads = []
    for row in topomap:
        for m in re.finditer("0",row):
            print(str(rownum) + "," + str(m.start()))
            trailheads.append((rownum,int(m.start()),0))
        rownum += 1
    return trailheads

# This function uses recursion to traverse multiple paths. Rather than keep
# track of direction from the previous step it just tries all 4 directions and
# only continues if it's height is 1 higher. It uses a list to keep track of steps
# already visited on a path so as to not double count equivilent paths.
def findscore(topomap,posy,posx,visited):
    if 'score' not in vars() and 'score' not in globals():
        # I could not get this function to work if I defined score outside the function
        # but defining it inside as a global seemed to work.
        global score
        score = 0
    height = int(topomap[posy][posx])
    if debug: print("Checking: " + str(posx) + "," + str(posy) + "," + str(height))
    if str(str(posy) + "," + str(posx)) in visited:
        return
    elif height == 9:
        score += 1
        #visited.append(str(str(posy) + "," + str(posx)))
        return
    else:
        # Move up
        if ( posy > 0 and int(topomap[posy-1][posx]) == height + 1  ):
            if debug: print("Moving up...")
            findscore(topomap,posy-1,posx,visited)
        # Move right
        if ( posx < len(topomap[0]) - 1 and int(topomap[posy][posx+1]) == height + 1  ):
            if debug: print("Moving right...")
            findscore(topomap,posy,posx+1,visited)
        # Move down
        if ( posy < len(topomap) - 1 and int(topomap[posy+1][posx]) == height + 1  ):
            if debug: print("Moving down...")
            findscore(topomap,posy+1,posx,visited)
        # Move left
        if ( posx > 0 and int(topomap[posy][posx-1]) == height + 1  ):
            if debug: print("Moving left...")
            findscore(topomap,posy,posx-1,visited)
        if debug: print("Nextscore: " + str(score) )
    if debug: print("Score: " + str(score))
    #visited.append(str(str(posy) + "," + str(posx)))
    return score

topomap = readfile()
printmap(topomap)
trailheads = findtrailheads(topomap)
for trailhead in trailheads:
    visited = []
    findscore(topomap,trailhead[0],trailhead[1],visited)
print(score)
