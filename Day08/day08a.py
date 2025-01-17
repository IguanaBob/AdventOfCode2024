#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 08, Part 1
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
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################
#
# ChatGPT's summary:
# The map contains antennas with various frequencies, and antinodes occur
# at specific locations where two antennas of the same frequency are aligned
# such that one antenna is twice as far away as the other. For each pair of
# antennas with the same frequency, antinodes are created at two locations,
# one on either side of them. Your task is to calculate the number of unique
# locations on the map that contain an antinode.
#
# My Reflection:
# This used some of the same logic for building and workign with a map that
# Day 06 and others used, so it wasn't too hard. The search functionality
# remind me of the XMAS word search as well. Easy enough.
# 
# Some of the functions around creating and displaying maps is not really
# needed, but it made testing and visualizing the logic easier for me.
#
###############################################################################

import sys
import copy
import re

# I tried doing this with reg-ex but couldn't get it working. I went the quick
# lazy route to focus on the rest of the code. Should I re-write this later
# I'll do it properly.
scannable_freqs = ( "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9" )

# Allow specifying the input file for testing
if (len(sys.argv) > 1):
    inputfile = sys.argv[1]
else:
    inputfile = "input"

def readinput(inputfile):
    rows=[]
    with open(inputfile,"r") as file:
        for row in file:
            rows.append(row.strip())
    return rows

def showmap(radarmap):
    for row in radarmap:
        print("".join(row))
    return

def init_antimap(radarmap):
    width=len(radarmap)
    antimap = []
    for row in radarmap:
       antimap.append(list("." * len(row)))
    return antimap

def init_combined(radarmap):
    width=len(radarmap)
    antimap = []
    for row in radarmap:
       antimap.append(list(row))
    return antimap

def showantimap(antimap):
    for row in antimap:
        print("".join(row))
    return

def setantinode(antimap,y,x):
    print("Setting anti-node: " + str(x) + "," + str(y))
    if( x >= 0 and y >= 0 and x < len(antimap) and y < len(antimap[0]) ):
        print("Setting anti-node: " + str(x) + "," + str(y))
        if(antimap[y][x] == "."): antimap[y][x] = "#"
    return

def findantinodes(scanned):
    antinodes = []
    n = 0
    while n < len(scanned) - 1:
        m = n + 1
        while m < len(scanned):
            n1 = scanned[n]
            n2 = scanned[m]
    #        print(str(n1) + " ? " + str(n2))
            if ( n1[1] > n2[1] ):
                xdiff = (n1[1] - n2[1])
                an1x = n1[1] + xdiff
                an2x = n2[1] - xdiff
            else:
                xdiff = (n2[1] - n1[1])
                an1x = n1[1] - xdiff
                an2x = n2[1] + xdiff
            if ( n1[0] > n2[0] ):
                ydiff = (n1[0] - n2[0])
                an1y = n1[0] + ydiff
                an2y = n2[0] - ydiff
            else:
                ydiff = (n2[0] - n1[0])
                an1y = n1[0] - ydiff
                an2y = n2[0] + ydiff
            a1 = (an1x,an1y)
            a2 = (an2x,an2y)
#        print("X-diff: " + str(xdiff))
#        print("Y-diff: " + str(ydiff))
#        print("Anti-node 1: " + str(a1))
#        print("Anti-node 2: " + str(a2))
            antinodes.append((an1x,an1y))
            antinodes.append((an2x,an2y))
            m += 1
        n += 1
    return antinodes

def scan_freqs(radarmap,all_freqs):
    print("Scanning...")
    freqs = {}
    y = 0
    while y < len(radarmap[0]):
        x = 0
        while x < len(radarmap):
            loc_freq = radarmap[y][x]
            #print(str(x) + "," + str(y) + ":" + radarmap[y][x])
            if str(loc_freq) in all_freqs:
                # print("Found freq: " + loc_freq)
                if loc_freq in freqs:
                    freqs[loc_freq].append((x,y))
                else:
                    freqs.update({loc_freq:[]})
                    freqs[loc_freq].append((x,y))
            x += 1
        y += 1
        #print(freqs)
    return freqs

def show_freq(freqs,freq):
    if str(freq) in freqs:
        return freqs[str(freq)]
    else:
        return ()

def count_antinodes(antimap):
    antinodes=0
    for row in antimap:
        for char in row:
#            print(char)
            if char == "#":
                antinodes += 1
    return antinodes

radarmap = readinput(inputfile)
antimap = init_antimap(radarmap)
combinedmap = init_combined(radarmap)
#showmap(radarmap)
#showantimap(antimap)
scanned_freqs = scan_freqs(radarmap,scannable_freqs)
for f in scanned_freqs:
    print(str(f) + " " + str(show_freq(scanned_freqs,f)))
    antinodes = findantinodes(show_freq(scanned_freqs,f))
    print(str(f) + " anti-nodes: " + str(antinodes))
    for antinode in antinodes:
        setantinode(antimap,int(antinode[0]),int(antinode[1]))
        setantinode(combinedmap,int(antinode[0]),int(antinode[1]))
showmap(radarmap)
print("")
showmap(antimap)
print("")
showmap(combinedmap)
#showantimap(antimap)
print("Total antinodes: " + str(count_antinodes(antimap)))
