#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 04, Part 2
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
# The task has shifted from finding the word "XMAS" to finding two instances
# of "MAS" arranged in the shape of an X. Each MAS can appear forwards or
# backwards, and the X shape can occur in any orientation. Your goal is to
# count how many times an "X-MAS" appears in the word search, where the two
# MAS are arranged in an X shape.
#
# My Reflection:
# Not your Grandma's wordsearch, maybe. Now we need X shaped "words", and you
# would think this would complicate the logic, but really it simplified it as
# there was less things to check even though the shape is no longer a line so
# there is only one check loop instead of multiple.
#
###############################################################################

import re

def xmassearch(lines):
    found = 0   

    print(str(len(lines[0])) + "x" + str(len(lines)))

    print("Searching for X-shaped MAS blocks")
    x = 0
    y = 0
    while( y < len(lines) - 2):
        x = 0
        while ( x < len(lines[0]) - 2 ):
            if( lines[y+1][x+1] == "A" ):
                if( lines[y][x] == "M" and lines[y+2][x] == "M" and lines[y][x+2] == "S" and lines[y+2][x+2] == "S" ):
                   found = found + 1
                if( lines[y][x] == "M" and lines[y+2][x] == "S" and lines[y][x+2] == "M" and lines[y+2][x+2] == "S" ):
                   found = found + 1
                if( lines[y][x] == "S" and lines[y+2][x] == "S" and lines[y][x+2] == "M" and lines[y+2][x+2] == "M" ):
                   found = found + 1
                if( lines[y][x] == "S" and lines[y+2][x] == "M" and lines[y][x+2] == "S" and lines[y+2][x+2] == "M" ):
                   found = found + 1
            x = x + 1
        y = y + 1
    return(found)


line = []
lines = []
with open('input', 'r') as file:
    for line in file:
        lines.append(list(line.strip()))

totalfound = xmassearch(lines)
print(str(totalfound))
