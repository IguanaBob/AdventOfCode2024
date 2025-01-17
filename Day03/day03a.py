#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 03, Part 1
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
# The North Pole Toboggan Rental Shop's computer has corrupted memory with
# mixed valid and invalid instructions. The goal is to identify and sum the
# results of valid multiplication instructions (mul(X,Y)), ignoring any
# invalid characters or malformed instructions. Your task is to scan the
# corrupted memory, extract valid mul instructions, and calculate the total
# sum of the multiplications.
#
# My Reflection:
# On the Python re-write I went the traditional coding route, which was much
# simpler. Store the multiplcation commands in a list, split it, then multiply
# and add together. Easy enough.
#
###############################################################################

import re

total = 0

with open('input', 'r') as file:
    for line in file:
        for cmnd in (re.findall("mul\([0-9]+[0-9]?[0-9]?,[0-9]+[0-9]?[0-9]?\)", line)):  # find mul() commands
            nums = re.sub("(mul\(|\))","",cmnd.strip()).split(",")  # strip out all but ###,###, store in nums
            total = total + ( int(nums[0]) * int(nums[1]) )

print(total)
exit(0)
