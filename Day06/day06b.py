###############################################################################
#
# 2024 Advent of Code, Day 06, Part 2
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
# You should have received a copy of the GNU General Affero Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>. 
#
###############################################################################
#
# Reflection:
# This gave a good challenge over part 1. I stored every guard step including
# direction in a list to compare against for detecting looped paths.
#
# The function print_map will show the current map including with color coding.
# If this is printed every step it gives a nice animation for vizualizing the
# guard's path. I used this to ensure my movement logic worked as expected.
#
# If I was to redo this from scratch rather than base it on part-1 I would probably 
# have it just check entire rows/columns for obstructions each time it turns rather
# than test each step one by one to speed it up.
# This version takes several minutes to run.
#
###############################################################################

import re
import copy
import time

rows = []
position_log = []
positions = 1
block_list = []

# Find and returns the guard's current position
def find_position():
    row = 0
    while ( row < len(rows) ):
        result = re.search("(\^|\<|\>|V)","".join(rows[row]))
        if ( result ):
            col = result.start()
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
    direction = (show_position(int(position[0]),int(position[1])))
    next_position = find_next_position(int(position[0]),int(position[1]),direction).split(",")
    next_position_item = show_position(int(next_position[0]),int(next_position[1]))
    if ( next_position_item == "?" ):
        return(0)
    while ( next_position_item == "#"):
        if(direction == "<"): direction = "^"
        elif(direction == "^"): direction = ">" 
        elif(direction == ">"): direction = "V" 
        elif(direction == "V"): direction = "<" 
        next_position = find_next_position(int(position[0]),int(position[1]),direction).split(",")
        next_position_item = show_position(int(next_position[0]),int(next_position[1]))
    next_position_log = str(next_position[0]) + "," + str(next_position[1]) + "," + str(direction)
    if ( next_position_log in position_log ):
        print("Loop detected!")
        return("L")
    rows[int(position[0])][int(position[1])] = "X"
    rows[int(next_position[0])][int(next_position[1])] = direction
    position_log.append(str(next_position[0]) + "," + str(next_position[1]) + "," + str(direction))
    if ( ( str(next_position[0]) + "," + str(next_position[1]) ) not in block_list ):
        block_list.append(str(next_position[0]) + "," + str(next_position[1]))
    # # Uncomment the next line to vizually animate the guards' paths.
    # print_map( int(int(position[0]) - 25) , int(int(position[0]) + 25) )
    return(next_position_item)

# Print the map between rows "start" and "end"
def print_map(start,end):
    current_row = 0
    print("\n" * 30)
    for row in rows:
        if(current_row > start and current_row < end):
            print("".join(row).replace("^","\033[92m^\033[0m").replace(">","\033[92m>\033[0m").replace("<","\033[92m<\033[0m").replace("V","\033[92mV\033[0m").replace("#","\033[91m#\033[0m"))
        current_row = current_row + 1
    if(int(end) > int(len(rows) - 30)):
        print("\n" * (len(rows) - end))
    time.sleep(.04)  # Change to adjust the speed of the animation if looping

# # Returns the character stored at a particular position.
# If ? is returned, it is assumed this is outside the boundries of the map.
# r=row=y, c=column=x
def show_position(r,c):
    if ( int(r) > int(len(rows[0])-1) or int(c) > int(len(rows)-1) or int(r) < 0 or int(c) < 0 ):
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
        if ( int(c) > int( len(rows[0]) - 1) ):
            return("?")
        else:
            return( str(r) + "," + str(int(c)+1) )
    elif ( d == "^"):
        if ( int(r) < 0 ):
            return("?")
        else:
            return( str(int(r)-1) + "," + str(c) )
    elif ( d == "V"):
        if ( int(r) > int( len(rows) - 1 ) ):
            return("?")
        else:
            return( str(int(r)+1) + "," + str(c) )

with open("input","r") as file:
    for line in file:
        rows.append(list(line.strip()))

original_rows = copy.deepcopy(rows)

next_step = ""

position = (find_position().split(","))
orig_position = position.copy()

# Run once to create step log
while(next_step != 0 and next_step != "L"):
    position = (find_position().split(","))
    next_step = take_step()

position = orig_position.copy()
pos_log_copy = copy.deepcopy(position_log)
total_blockables = 0
position_log = []
z=0
block_list_copy = block_list.copy()

print("Block list length: " + str(len(block_list)))
for block_spot in block_list_copy:
    rows = copy.deepcopy(original_rows)
    position = orig_position.copy()
    block_pos = block_spot.split(",")
    rows[int(block_pos[0])][int(block_pos[1])] = "#"
    print("Blocking: " + str(block_pos) )
    print(str(z) + " of " + str(len(block_list_copy)) )
    next_step = ""
    while(next_step != 0 and next_step != "L"):
        position = (find_position().split(","))
        next_step = take_step()
        if ( next_step == "L" ):
            total_blockables = total_blockables + 1

    # The Answer
    # Total number of blocking positions that end in a loop path
    # This prints every iteration, so the answer will be the last one printed.
    print("Total loops: " + str(total_blockables) )
    position_log = []
    z = z + 1

