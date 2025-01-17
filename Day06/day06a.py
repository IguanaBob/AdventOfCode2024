#!/usr/bin/python3

###############################################################################
#
# 2024 Advent of Code, Day 06, Part 1
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
# The Historians travel back to 1518 to a lab with a guard patrolling the area.
# The guard follows a strict protocol: if there's an obstacle in front, they
# turn right; otherwise, they move forward. Your task is to predict the guard's
# path and count how many distinct positions the guard will visit before leaving
# the mapped area.
#
# My Reflection:
# Part 1 was not particularly hard. Was good pracitce on matrices/nested lists.
#
###############################################################################

import re

rows = []     # Stores the map
positions = 1 # Initialize with 1 to count the starting position.

# Find and returns the guard's current position
def find_position():
    row = 0
    while ( row < len(rows) ):
        result = re.search("(\^|\<|\>|V)","".join(rows[row]))
        if ( result ):
            col = result.start()
            #print( "Found at row " + str(row) + ", column " + str(col) )
            return( str(row) + "," + str(col) )
        row = row + 1
    return(1)

# Set the character stored at a position
def set_position(r,c,item):
    rows[r][c] = item
    return 0

# Take a step in the direction faced, return the next position's item
def take_step():
    position = (find_position().split(","))
    #print(position)
    direction = (show_position(int(position[0]),int(position[1])))
    #print("Current: " + str(position) + ": " + direction )
    print("Current: " + str(position[0]) + "," + str(position[1]) + ": " + direction )
    print("Positions: " + str(positions) )
    next_position = find_next_position(int(position[0]),int(position[1]),direction).split(",")
    next_position_item = show_position(int(next_position[0]),int(next_position[1]))
    print("Next: " + str(next_position[0]) + "," + str(next_position[1]) + ": " + next_position_item )
    if ( next_position_item == "?" ):
        return(0)
    while ( next_position_item == "#"):
        if(direction == "<"): direction = "^"
        elif(direction == "^"): direction = ">" 
        elif(direction == ">"): direction = "V" 
        elif(direction == "V"): direction = "<" 
        next_position = find_next_position(int(position[0]),int(position[1]),direction).split(",")
        next_position_item = show_position(int(next_position[0]),int(next_position[1]))
        print("Next: " + str(next_position[0]) + "," + str(next_position[1]) + ": " + next_position_item )
    rows[int(position[0])][int(position[1])] = "X"
    rows[int(next_position[0])][int(next_position[1])] = direction
    #print(show_position(int(position[0]),int(position[1])))
    #print(next_position_item)
    return(next_position_item)

# Returns the character stored at a particular position.
# If ? is returned, it is assumed this is outside the boundries of the map.
# r=row=y, c=column=x
def show_position(r,c):
    if ( int(r) > len(rows[0]) or int(c) > len(rows) or int(r) < 0 or int(c) < 0 ):
            return("?")
    elif ( rows[r][c] in ("<",">","^","V","#",".","X") ):
            return(rows[r][c])
    return("?")

# Pass a coordiante and direction, returns the next position coordinates in r,c format
# < > V ^ = guard's current position and direction faced
# . = open position
# # = obstacle
# X = already visited location
# ? = off the map
def find_next_position(r,c,d):
    if ( d not in ["<",">","^","V","#",".","X"] ):
        return("?")
    elif ( d == "<" ):
        if ( int(c) < 0 ):
            return("?")
        else:
            return( str(r) + "," + str(int(c)-1) )
    elif ( d == ">" ):
        if ( int(c) > len(rows[0]) ):
            return("?")
        else:
            return( str(r) + "," + str(int(c)+1) )
    elif ( d == "^"):
        if ( int(r) < 0 ):
            return("?")
        else:
            return( str(int(r)-1) + "," + str(c) )
    elif ( d == "V"):
        if ( int(r) > len(rows) ):
            return("?")
        else:
            return( str(int(r)+1) + "," + str(c) )

with open("input","r") as file:
    for line in file:
        rows.append(list(line.strip()))

next_step = ""
while(next_step != 0):
    position = (find_position().split(","))
    next_step = take_step()
    if ( next_step != "X" and next_step != 0): positions = positions + 1

# The answer for Day 6, part 1.
# Number of unique guard positions before leaving the map.
print("Positions: " + str(positions))

