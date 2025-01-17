#!/usr/bin/python3

###############################################################################
#
# 2024 Advent of Code, Day 01, Part 1
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
# The Chief Historian has gone missing, and a group of
# Elvish Senior Historians is tasked with finding him by checking
# historically significant locations. They have two incomplete lists of
# location IDs, and your job is to calculate the total distance between
# these lists by pairing up the smallest numbers from each list and summing
# the differences between corresponding pairs. The total distance will help
# them reconcile the lists and find the missing historian.
# 
# My Reflection:
# Again, not hard. This was just a re-write using Python as I changed what
# language I wanted to focus on practicing.
#
# As I had wanted, on the re-write I allowed for an input file of any length.
#
###############################################################################

list0 = []
list1 = []
with open('input', 'r') as file:
    for line in file:
        list0.append(int(line.strip().split()[0]))
        list1.append(int(line.strip().split()[1]))

list0.sort()
list1.sort()

len0 = len(list0)
len1 = len(list1)

i = 0
total = 0
while ( i < len0 ):
    difference = abs( list0[i] - list1[i] )
    total = total + difference
    print(str(list0[i]) + " - " + str(list1[i]) + " = " + str(difference) )
    i = i + 1

# The answer
# Total of the difference between the two sorted lists.
print("Difference total = " + str(total))
