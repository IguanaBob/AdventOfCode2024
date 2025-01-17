#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 07, Part 2
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
# The engineers discover a third operator, the concatenation operator (||), 
# which combines the digits from its left and right inputs into a single 
# number. All operators, including +, *, and ||, are evaluated left-to-right. 
# Your task is to find all the equations that can be made true using these 
# operators, then sum the test values from the valid equations to determine 
# the new total calibration result.
#
# My Reflection:
# Using product() from itertools cleaned up my operator list generation quite a
# bit. The hard part with part 2, though, was figuring out the logic to make
# the concatenate operator work. Initially I miss-understood how it was
# supposed to function, thinking it would calculate the right side of the
# operator before concatinating, and I wrote a complicated recursive function
# to make this work. After many attempts and failures to get the correct answer
# on yet another re-read of the instructions I realized I was misinterpreting
# the explanation of how this operator worked and it was to be handled
# left-to-right just like the others. I then ripped out the recursive function
# and wrote it properly. Much simpler, but practicing recurstion is something
# I needed anyway, so I still got something out of it. Always look on the
# bright side.
#
###############################################################################

import sys
from itertools import product

# Allow specifying the input file for testing
if (len(sys.argv) > 1):
    inputfile = sys.argv[1]
else:
    inputfile = "input"

total_calibration_result = 0

# Check if equation is valid
def solve(nums,ops):
    i = 0
    solution = nums[0]  # Initialize solution to the first figure in the equation
    while( (i < len(nums) - 1)):  # Check the operands one by one and handle the next figure accordingly, storing in solution.
        if (ops[i] == "C"): solution = int( str(solution) + str(nums[i+1]) )  # Concatenate by converting to strings.
        # I had an alternative version of this that would multiple the first number by 10^length of the second,
        # and I even had it working. However, this was before the recursion debacle was resolved and on the
        # re-write of solve() I ended up going with the simpler solution of converting to strings.
        elif (ops[i] == "+"): solution += nums[i+1]  # Add
        else: solution *= nums[i+1]  # Multiply
        i += 1
    return solution

# Read input file
with open(inputfile,"r") as file:
    for line in file:
        answer = int(line.split(":")[0])
        equation = tuple(map(int,line.split()[1:]))

        # Iterate through every combination of operators, checking each possible equation with solve()
        # C represents concatenate, ||
        for ops in product("+*C", repeat=(len(equation)-1)):
            found = False
            # If equation is valid, add to the sum and break out of loop
            if ( answer == solve(equation,ops) ):
                total_calibration_result += answer
                break

print("Total calibration result: " + str(total_calibration_result))
