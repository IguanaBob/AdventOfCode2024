#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 04, Part 1
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
# In the Ceres monitoring station, you help an Elf with a word search to
# find all instances of the word "XMAS". The word can appear in any direction:
# horizontal, vertical, diagonal, forwards, backwards, or even overlapping.
# Your task is to count how many times "XMAS" appears in the word search.
#
# My Reflection:
# It's a child's word search, but harder, unless you do it in code. I simply
# did a search in each direction using x/y coordinates and adding 1 or -1 to
# the start position, then moved to the next postion. Not the most efficient,
# but it was easy to get working.
#
###############################################################################

import re

def xmassearch(lines):
    found = 0   

    print(str(len(lines[0])) + "x" + str(len(lines)))

    print("Searching Horizontally")
    x = 0
    y = 0
    while( y < len(lines)):
        x = 0
        while ( x < len(lines[0]) - 3 ):
#            print("Line " + str(y) + " Chars " + str(x) + " to " + str(( x + 4 )))
#            print( str(lines[y][x]) + str(lines[y][x+1]) + str(lines[y][x+2]) + str(lines[y][x+3]) )
            if( str(lines[y][x]) == "X" and str(lines[y][x+1]) == "M" and str(lines[y][x+2]) == "A" and str(lines[y][x+3]) == "S" ):
#                print("MATCH")
                found = found + 1
            if( str(lines[y][x]) == "S" and str(lines[y][x+1]) == "A" and str(lines[y][x+2]) == "M" and str(lines[y][x+3]) == "X" ):
                found = found + 1
            x = x + 1
        y = y + 1
    print(found)

    print("Searching Verically")
    x = 0
    y = 0
    while( x < len(lines[0])):
        y = 0
        while ( y < len(lines) - 3 ):
            if( str(lines[y][x]) == "X" and str(lines[y+1][x]) == "M" and str(lines[y+2][x]) == "A" and str(lines[y+3][x]) == "S" ):
                found = found + 1
            if( str(lines[y][x]) == "S" and str(lines[y+1][x]) == "A" and str(lines[y+2][x]) == "M" and str(lines[y+3][x]) == "X" ):
                found = found + 1
            y = y + 1
        x = x + 1
    print(found)

    print("Searching Diagonally")
    x = 0
    y = 0
    while( y < len(lines) - 3):
        x = 0
        while ( x < len(lines[y]) - 3 ):
            if( lines[y][x] == "X" and lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S" ):
                found = found + 1
            if( lines[y][x] == "S" and lines[y+1][x+1] == "A" and lines[y+2][x+2] == "M" and lines[y+3][x+3] == "X" ):
                found = found + 1
            if( lines[y][x+3] == "X" and lines[y+1][x+2] == "M" and lines[y+2][x+1] == "A" and lines[y+3][x] == "S" ):
                found = found + 1
            if( lines[y][x+3] == "S" and lines[y+1][x+2] == "A" and lines[y+2][x+1] == "M" and lines[y+3][x] == "X" ):
                found = found + 1
            x = x + 1
        y = y + 1
    print(found)

    return(found)


line = []
lines = []
with open('input', 'r') as file:
    for line in file:
        lines.append(list(line.strip()))

totalfound = xmassearch(lines)
print(str(totalfound))
