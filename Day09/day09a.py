###############################################################################
#
# 2024 Advent of Code, Day 09, Part 1
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
# Reflection:
# This part was not very difficult, but was interesting. It gave some good
# practice on list manipulation.
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

with open(inputfile,"r") as file:
    print("Reading input...")
    while True:
        filesize = file.read(1)
        if not filesize or not filesize in list("0123456789"):
            break
        else:
            if (int(filesize) > 0):
                fs = int(filesize)
                while ( fs > 0 ):
                    output.append(int(filecount))
                    fs -= 1
            filecount += 1

        freesize = file.read(1)
        if not freesize or not freesize in list("0123456789"):
            break
        elif ( int(freesize) > 0 ):
            fs = int(freesize)
            while ( fs > 0 ):
                output.append(".")
                fs -= 1

disksize = len(output)

# Compact
print("Compacting...")
while("." in output):
    popped = output.pop(-1)
    if "int" in str(type(popped)):
        output[output.index(".")] = popped

# Fill end of map with "."
# This is not needed for checksum so it is commented out.
#while ( len(output) < disksize ):
#    output.append(".")

# Checksum
print("Calculating checksum...")
pos = 0
checksum = 0
while(pos < len(output)):
    if str(output[pos]) != ".":
        checksum += ( pos * output[pos] )
    pos += 1
print("Checksum: " + str(checksum))
