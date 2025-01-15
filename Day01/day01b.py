#!/usr/bin/python3

###############################################################################
#
# 2024 Advent of Code, Day 01, Part 2
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
# ChatGPT's summary:
# The Historians discover that many location IDs appear in both lists,
# suggesting that some numbers may have been misinterpreted. This time,
# you need to calculate a similarity score by multiplying each number from
# the left list by how many times it appears in the right list, then summing
# all these products. The final score will provide insight into how similar
# the two lists really are.
#
# My Reflection:
# Same basic logic as the Bash version, I just use basic Python math functions
# for the counting and multiplication. Nothing too interesting.
#
###############################################################################

list0 = []
list1 = []
with open('input', 'r') as file:
    for line in file:
        list0.append(int(line.strip().split()[0]))
        list1.append(int(line.strip().split()[1]))

len0 = len(list0)
len1 = len(list1)
if ( len0 != len1):
    exit("Error: lists are different lengths")

i = 0
total = 0
while ( i < len0 ):
    c = 0
    j = 0
    while ( j < len0 ):
        if ( list0[i] == list1[j] ):
                c = c + 1
        j = j + 1
    total = total + list0[i] * c
    i = i + 1

# The answer, Sum of the product of each number from the first list and the number
# of times that number appears in the second list.
print("Total: " + str(total))
