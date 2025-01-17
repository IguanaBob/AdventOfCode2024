#!/bin/bash

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
# Fairly easy using simple bash commands. Not much to say.
#
# If I was to rewrite I would not hardcode the forloop length but let it run on
# A file of any length.
#
# My initial version of this had the input file split and sorted manually ahead
# of time into seperate files. I later decided this was against the spirit and
# re-wrote it to do all processing within the script.
#
###############################################################################

input="input"

show_number ( ) {
    file=$1
    line=$2
    column=$3
    cat ${file} | awk -v c1=$column '{ print $c1 }' | sort -n | head -${line} | tail +${line}
}

total=0
for (( i=1 ; $i<=1000 ; i++ )); do	{
	total=$(( $( echo "$( show_number $input $i 1)-$( show_number $input $i 2 )" | bc | sed 's/-//g' ) + ${total} ))
}
done

# The answer
# Total of the difference between the two sorted lists.
echo $total
