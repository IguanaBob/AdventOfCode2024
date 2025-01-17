#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 08, Part 2
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
# After accounting for resonant harmonics, antinodes now occur at any grid 
# position aligned with at least two antennas of the same frequency, including 
# the positions of the antennas themselves (unless it's the only antenna of 
# that frequency). Your task is to calculate the total number of unique 
# locations containing an antinode on the map based on this updated model.
#
# My Reflection:
# Extending part 1 presented a challenge as for some reason I had trouble
# getting the logic around calculating far antinodes working correctly.
# Not much to say for a solution other than it took a bit of brute-force
# hacking at it for a while to find the flaws in the logic.
#
###############################################################################

import sys
import copy
import re

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
    if( x >= 0 and y >= 0 and x < len(antimap) and y < len(antimap[0]) ):
        antimap[y][x] = "#"
    return

def findantinodes(scanned):
    antinodes = []
    n = 0
    while n <= len(scanned)+1 :
        m = n + 1
        while m < len(scanned) :
            n1 = scanned[n]
            n2 = scanned[m]
            xdiff = (n1[1] - n2[1])
            ydiff = (n1[0] - n2[0])
            c=0
            while(c < 55):
                antinodes.append(((n1[1]+(xdiff*c)),(n1[0]+(ydiff*c))))
                antinodes.append(((n1[1]-(xdiff*c)),(n1[0]-(ydiff*c))))
                c += 1
            d=0
            while(d < 55):
                antinodes.append(((n1[1]+(xdiff*d)),(n1[0]+(ydiff*d))))
                antinodes.append(((n1[1]-(xdiff*d)),(n1[0]-(ydiff*d))))
                d += 1
            m += 1
        n += 1
    return antinodes

def scan_freqs(radarmap,all_freqs):
    freqs = {}
    y = 0
    while y < len(radarmap[0]):
        x = 0
        while x < len(radarmap):
            loc_freq = radarmap[y][x]
            if str(loc_freq) in all_freqs:
                if loc_freq in freqs:
                    freqs[loc_freq].append((x,y))
                else:
                    freqs.update({loc_freq:[]})
                    freqs[loc_freq].append((x,y))
            x += 1
        y += 1
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
            if char == "#":
                antinodes += 1
    return antinodes

radarmap = readinput(inputfile)
antimap = init_antimap(radarmap)
combinedmap = init_combined(radarmap)
scanned_freqs = scan_freqs(radarmap,scannable_freqs)
for f in scanned_freqs:
    antinodes = findantinodes(show_freq(scanned_freqs,f))
    for antinode in antinodes:
        setantinode(antimap,int(antinode[0]),int(antinode[1]))
        setantinode(combinedmap,int(antinode[0]),int(antinode[1]))
showmap(radarmap)
print("")
showmap(antimap)
print("")
showmap(combinedmap)
print("Total antinodes: " + str(count_antinodes(antimap)))
