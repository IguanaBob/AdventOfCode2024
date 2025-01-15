#!/bin/bash

###############################################################################
#
# 2024 Advent of Code, Day 02, Part 1
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
# The Red-Nosed Reindeer nuclear fusion plant needs help analyzing data
# from reports that contain lists of numbers, called levels. A report is
# considered safe if the levels are either all increasing or all decreasing,
# and any two adjacent levels differ by at least 1 and at most 3. Your task
# is to determine how many reports are safe based on these rules.
#
# My Reflection:
# I don't like my bash here, they way it reads through the list using head/tail
# is slow and inefficient as it re-reads the file numerous times, but it works.
#
###############################################################################

file=input
filelength=$( wc -l ${file} | awk '{ print $1}' )

show_report () {
	report=${1}
	head -${report} ${file} | tail +${report}
}

levels_in_report () {
	show_report $1 | wc -w | awk '{ print $1 }'
}

show_report_level () {
	level=${2}
	show_report $1 | awk -v f1=${level} '{ print $f1 }'
}

safe_reports=0
for (( i=1 ; $i <= ${filelength} ; i++ )); do {
	show_report $i
	if [ $(show_report_level $i 1) -lt $(show_report_level $i 2) ]; then
		direction=gt
	elif [ $(show_report_level $i 1) -eq $(show_report_level $i 2) ]; then
		direction=eq
	else
		direction=lt
	fi
	for (( j=1 ; $j < $(( $( levels_in_report ${i}) )) ; j++ )); do {
		level=$( show_report_level $i $j )
		next_level=$( show_report_level $i $(( $j + 1 )) )
		if [ $next_level -eq $level ]; then
			echo "Unsafe! Adjacent levels equal. ($level = $next_level)"
			safe=0
			break
		elif [ ! $next_level -${direction} $level ]; then
			echo "Unsafe! Direction change or no change. ($level $direction $next_level)"
			safe=0
			break
		else
			if [ $( echo $(( $next_level - $level )) | sed s/-//g ) -gt 3  ]; then
				echo "Unsafe! Change greater than 3. ($next_level - $level = $( echo $(( $next_level - $level )) | sed s/-//g ))"
				safe=0
				break
			else
				safe=1
			fi
		fi
	}
	done
	if [ $safe -eq 1 ]; then
		echo Safe!
		safe_reports=$(( $safe_reports + 1))
	fi
}
	echo Reports checked: $i
	echo Safe so far: $safe_reports
done

# The answer, the total number of safe reports.
echo Total number of safe reports: $safe_reports
