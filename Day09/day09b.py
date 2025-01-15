#!/usr/bin/python3

###############################################################################
#
# 2024 Advent of Code, Day 09, Part 2
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
# You should have received a copy of the GNU General Affero Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>. 
#
###############################################################################
#
# ChatGPT's summary:
# The amphipod revises his plan to compact the disk by moving entire files
# instead of individual blocks. Each file is moved to the leftmost span of
# free space large enough to fit it, starting with the file with the highest
# ID number. If a file can't be moved due to insufficient space, it stays
# in its current position. After compacting, the filesystem checksum is
# calculated the same way by multiplying each block's position by its
# file ID and summing the results.
#
# My Reflection:
# Part 2 gave more of a challenge than part 1. The compact_map function took me
# 2-3 rewrites until I got it working properly and fast. I'm sure there is a
# more efficient method than manually searching earch position, but I wanted to
# do this day purely based on existing memory rather than reaching out to
# to documentation/search.
#
###############################################################################

import sys

# Allow specifying the input file for testing
if (len(sys.argv) > 1):
    inputfile = sys.argv[1]
else:
    inputfile = "input"

output = []
filecount = 0

def printmap(diskmap):
    for file in diskmap:
        print(str(file[0]) + "," + str(file[1]))
    return

# I ended up not using this as I later integrated the free space merge checks into the file move operations,
# but I thought it was interesting so I am leaving it here to view.
#
#def merge_free_space(diskmap):
#    print("Merging free space, 1 itereation...")
#    freepos = 0
#    merged = False
#    while ( freepos < len(diskmap)-1):
#        if (diskmap[freepos][0] == "." and diskmap[freepos+1][0] == "." ):
#            print("Merging adjacent free spaces at " + str(freepos) + " (" + str(diskmap[freepos][1]) + ") and " + str(freepos+1) + " (" + str(diskmap[freepos+1][1]) + ")" )
#            freesize1 = int(diskmap[freepos][1])
#            freesize2 = int(diskmap[freepos+1][1])
#            diskmap.pop(freepos)
#            diskmap.pop(freepos)
#            diskmap.insert(freepos,[".",str(freesize1 + freesize2)])
#            merged = True
#            return merged
#            break
#        freepos += 1
#    return merged

def compactmap(diskmap):
    # Compact the disk
    # I'm sure there is a more effiecient way to do this with python's search functions.
    print("Compacting...")
    lastmoved = int(filecount)
    tocheck = int(filecount)-1
    # Check each ID from largest to 0
    while(tocheck >= 0):
        pos = len(diskmap)-1
        # Search for the location of the file (this can probably be optimized)
        while(pos > 0):
            if ( str(diskmap[pos][0]) == str(tocheck) and tocheck < lastmoved ):
                freepos = 0
                print("Checking " + str(tocheck))
                filesize = int(diskmap[pos][1])
                # Find a free space large enough to hold the file
                while (freepos < pos and str(tocheck) and tocheck < lastmoved ):
                    if ( str(diskmap[freepos][0]) == "." ):
                        freesize = int(diskmap[freepos][1])
                        # Free space found
                        if ( freesize >= filesize):
                            # Begin moving file
                            popped = diskmap.pop(pos)
                            freepopped = diskmap.pop(freepos)
                            diskmap.insert(freepos,popped)
                            # Handle free space
                            if ( freesize > filesize):
                                # Restore remaining free space after file
                                diskmap.insert(freepos+1,[".",str(freesize - filesize)])
                            else:
                                pos -= 1
                            # Handle free space in file's original location
                            if ( pos == len(diskmap) - 1 ):
                                # File was at end
                                if ( str(diskmap[pos][0]) == "." ):
                                    # Free space before, file at end
                                    diskmap[pos][1] = str( int(diskmap[pos][1]) + filesize )
                                else:
                                    # No free space before, file at end
                                    diskmap.append([".",str(filesize)])
                            elif ( pos < len(diskmap) - 1):
                                if ( str(diskmap[pos][0]) == "." and str(diskmap[pos+1][0]) == "." ):
                                    # Free space before and after
                                    diskmap[pos][1] = str( int(diskmap[pos][1]) + int(diskmap[pos+1][1]) + filesize )
                                    diskmap.pop(pos+1)
                                elif ( str(diskmap[pos][0]) == "." and str(diskmap[pos+1][0]) != "." ):
                                    # Free space before only
                                    diskmap[pos][1] = str( int(diskmap[pos][1]) + filesize )
                                elif ( str(diskmap[pos][0]) != "." and str(diskmap[pos+1][0]) != "." ):
                                    # No space before or after
                                    diskmap.insert(pos+1,[".",str(filesize)])
                                elif ( str(diskmap[pos][0]) != "." and str(diskmap[pos+1][0]) == "." ):
                                    # Free space after only
                                    diskmap[pos+1][1] = str( int(diskmap[pos+1][1]) + filesize )
                            lastmoved = tocheck
                            break
                    freepos += 1
                    if(tocheck >= lastmoved): break
            pos -= 1
        tocheck -= 1
    return diskmap

def diskchecksum(diskmap):
    # Checksum
    print("Calculating checksum...")
    pos = 0
    checksum = 0
    realpos = 0
    while(pos < len(diskmap)-1):
        if str(diskmap[pos][0]) != ".":
            i = 0
            while( i < int(diskmap[pos][1]) ):
                checksum += ( int(diskmap[pos][0]) * (realpos+i) )
                i += 1
        realpos += int(diskmap[pos][1])
        pos += 1
    print("Checksum: " + str(checksum))
    return

def readfile():
    with open(inputfile,"r") as file:
        print("Reading input...")
        filecount = 0
        while True:
            filesize = file.read(1)
            if not filesize or not filesize in list("0123456789"):
                break
            else:
                output.append([str(filecount),str(filesize)])
                filecount += 1
                print(filecount)
            freesize = file.read(1)
            if not freesize or not freesize in list("0123456789"):
                break
            elif ( int(freesize) > 0 ):
                output.append([".",str(freesize)])
    return filecount


filecount = readfile()
printmap(output)
diskchecksum(output)
compactmap(output)
printmap(output)
diskchecksum(output)
#printmap(output)
