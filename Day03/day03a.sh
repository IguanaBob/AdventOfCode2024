#!/bin/bash
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
# I did this one entirely on the command line in a one-liner and then saved it
# in the .sh once it was working. No reason for this other than to challenge
# myself to do it this way for fun and learning. I put an explination of each
# part of the one-liner at the bottom.
#
###############################################################################

# My original solution
# cat input | sed -e "s/mul(/\nmul(/g" | sed -e "s/)/)\n/g" | egrep "^mul\([0-9]+??,[0-9]+??\)$" | cut -f2 -d\( | cut -f1 -d\) | sed -e "s/,/*/g" | xargs -0 echo | bc | sed -e "s/$/+/g" | xargs | sed -e "s/ //g" | sed -e "s/+$//" | bc

# A shortened version while writing up the following explanation
cat input | sed -e "s/mul(/\nmul(/g" | sed -e "s/)/)\n/g" | egrep "^mul\([0-9]+??,[0-9]+??\)$" | cut -f2 -d\( | cut -f1 -d\) | sed -e "s/,/*/g" | bc | sed -e "s/$/+/g" | xargs | sed -e "s/+$//" | bc

## Explanation

## Read the input file
# cat input

# Break out instances of "mul(" onto new lines using sed.
# | sed -e "s/mul(/\nmul(/g"

# Break lines at ending )
# | sed -e "s/)/)\n/g"

# Filter for valid mul entries fitting the format mul(###,###) where ### is 1-3 numerals.
# | egrep "^mul\([0-9]+??,[0-9]+??\)$"

# Format lines into format "###,###" by cutting between the parens.
# | cut -f2 -d\(
# | cut -f1 -d\)

# Replace , with * to prepare output for bc calculator.
# | sed -e "s/,/*/g"

# Pass to bc to multiple.
# | bc

# Append + to the end of each calulation to begin formatting for another round of bc.
# | sed -e "s/$/+/g"

# Merge lines into one for bc
# | xargs

# Remove trailing + that was added to all lines by the previous sed
# | sed -e "s/+$//"

# Sum with bc
# | bc
