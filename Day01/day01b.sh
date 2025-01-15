#!/bin/bash

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
# Not too hard. I count simply by using "grep -c" on the 2nd list for each
# number on the first list. In the Bash version I again hardcoded a 1000 limit.
#
###############################################################################


input="input"

show_l1_number ( ) {
	line=$1
	cat list1 | head -${line} | tail +${line}
}

similarity=0
for (( i=1 ; $i<=1000 ; i++ )); do {
	num=$( show_l1_number $i )
	echo $num
	occurances=$( grep -c $num list2 )
	similarity=$(( $similarity + $(( $num * $occurances )) ))
}
done

# The answer, Sum of the product of each number from the first list and the number
# of times that number appears in the second list.
echo $similarity
