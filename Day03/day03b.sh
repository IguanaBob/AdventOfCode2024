#!/bin/bash
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
# Tracking the do() and don't() without variables really complicated this in,
# and this is where I regretted the one-liner idea. I kept going, though, to
# challenge myself. I ended up adding a multiplication by 1 or 0 and grouping
# instructions, with lots of complicated sed work, to make it work with bc.
# The only variables here are withing bc itself. Ugly, but one-liners are never
# very pretty.
#
###############################################################################

# An expanded Bash one-liner based on the part 1 version

# My original solution
( echo "0 " ; ( echo "x = 1; " ; ( cat input | sed -e "s/mul(/\nmul(/g" | sed -e "s/do(/\ndo(/g" | sed -e "s/don't(/\ndon\'t(/g" | sed -e "s/)/)\n/g" | egrep "^(mul\([0-9]+??,[0-9]+??\)|do(n't)?\(\))$" | sed -e "s/^do()/x = 1;/g" | sed -e "s/^don't()/x = 0;/g" | sed -e "s/^mul(/ if (x == 1) { (/g" | sed -e "s/,/*/g" | sed -e "s/)$/) } else { 0 + 0 };/g" ) ) | bc | sed -e "s/^/+ /g" ) | xargs | bc


## Explanation

# Wrap multiple commands in parens to merge otput for later processing, opening paren
# (

# Start by outputting "0 " to prevent a later sytax error with bc to deal with starting + on output passed to bc later
# echo "0 "

# Seperator between commands with merged output
# ;

# 2nd level text merging, opening paren
# ( 

# This output, when processed by bc, will set a variable "x" to 1  that is used as a conditional check to handle do() and don't() commands.
# do() will be when x is 1, and don't() when x = 0.
# We have to start with an explicit output of "x = 1;" here as we assume because of this part of the explanation "At the beginning of the program, mul instructions are enabled." and there is no starting do() in the input.
# echo "x = 1; "

# Seperator between commands with merged output
# ;

# 3rd level text merging, opening paren
# ( 

# Begin reading the input file
# cat input

# Break out mul(, do(, and don't( onto new lines with sed
# | sed -e "s/mul(/\nmul(/g"
# | sed -e "s/do(/\ndo(/g"
# | sed -e "s/don't(/\ndon\'t(/g"

# Break lines and ending )
# | sed -e "s/)/)\n/g"

# Filter for lines fitting the following formats only
# do()
# don't()
# mul(###,###) where ### is 1-3 numerals
# | egrep "^(mul\([0-9]+??,[0-9]+??\)|do(n't)?\(\))$"

# Replace do() with x = 1; and don't() with x = 0; to set x variable for bc's later conditional check (see explanation higher up)
# | sed -e "s/^do()/x = 1;/g"
# | sed -e "s/^don't()/x = 0;/g" 

# Prepend mul() commands with the conditional check for x = 1.
# | sed -e "s/^mul(/ if (x == 1) { (/g"

#  Replace , with * so be multiplies
# | sed -e "s/,/*/g"

# Append closing portion of the conditional started 2 steps above.
# In the else statement with force an ouput of 0.
# This completed conditional ensures that any multiplications that happen after don't() do not get summed by bc in the next steps.
# | sed -e "s/)$/) } else { 0 + 0 };/g" ) )

# Pass to bc to multiple each line
# | bc

# Add + between each line result of multiplication to prepare for summing.
# | sed -e "s/^/+ /g" )

# Merge lines to prepare for passing to bc
# | xargs

# Sum all previous caluclations for final answer
# | bc


## Possible further improvements:
## - Do all formatting earlier to allow for a single run of bc
## - Simplify by re-writing as a traditional script with bash variables, loops, and conditionals rather than relying on pipes and bc.
## - Use real regex to simplify search/verification/formatting
