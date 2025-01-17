#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 03, Part 2
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
# The corrupted memory already contained do() and don't() instructions, which
# enable or disable mul instructions, but they were previously ignored. Now,
# you need to consider these instructions, where only the most recent do() or
# don't() instruction applies. Initially, mul instructions are enabled. Your
# task is to sum the results of the enabled multiplications after applying
# the correct enable/disable logic.
#
# My Reflection:
# Only addition over part 1 is find do() and don't() commands and use them to
# set variable to 0 or 1 which causes mul() commands to be skipped if 1. I
# should have used a boolean here.
#
###############################################################################

import re

total = 0
do = 0

with open('input', 'r') as file:
    for line in file:
        for cmnd in (re.findall("(do\(\)|don't\(\)|mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\))", line)):  # find mul() commands
            #print(cmnd)
            if ( cmnd == str("do()") ):
                do = 0
            elif ( cmnd == str("don\'t()") ):
                do = 1
            elif ( do == 0 ):
                nums = re.sub("(mul\(|\))","",cmnd.strip()).split(",")  # strip out all but ###,###, store in nums
                answer = int(nums[0]) * int(nums[1])
                #print(nums[0] + " * " + nums[1] + " = " + str(answer) )
                total = total + answer
                #print("Total: " + str(total))

print(total)
exit(0)

