#!/bin/bash

###############################################################################
#
# 2024 Advent of Code, Day 02, Part 2
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
# The engineers introduce the Problem Dampener, which allows the reactor
# safety systems to tolerate a single bad level in a report. Now, the same
# rules apply, but if removing one level from an unsafe report makes it
# safe, the report counts as safe. Your task is to determine how many reports
# are now safe, considering this new tolerance for a single bad level.
#
# My Reflection:
# The dampening logic took a long time to get working, and it's ugly how I did
# it in bash.
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

check_if_safe () {
	# Check if passed array contains a safe report

	check_len=$#
	echo "Checking: ${@}"

	# Find Direction
	if [ $1 -lt $2 ]; then
		direction=gt
	elif [ $1 -eq $2 ]; then
		# echo "UNSAFE: Levels 1 and 2 are equal ($1 = $2)"
		return 1
	else
		direction=lt
	fi
	#echo "Direction: $direction"

	# Check if adjacent levels are equal
	for (( l=1 ; $l < $check_len ; l++ )); do
		nl=$(( $l + 1 ))
		level=${!l}
		next_level=${!nl}
		if [[ "$level" -eq "$next_level" ]]; then
			# echo "UNSAFE: Levels $l and $nl are equal ( $level = $next_level )"
			return 1
		elif [ ! $next_level -$direction $level ]; then
			# echo "UNSAFE: Direction changed. ( $next_level !$direction $level )"
			return 1
		elif [ $( echo "$(( $next_level - $level ))" | sed "s/-//g" ) -gt 3 ]; then
			# echo "UNSAFE: Change greater than 3. ($(( $next_level - $level )))"
			return 1
		fi
	done
#	echo "SAFE"
	return 0
}

safe_reports=0
for (( i=1 ; $i <= ${filelength} ; i++ )); do
	read -a report <<< "$(show_report $i)"  # Read report into an array
	levels=${#report[@]}
	echo "Report: ${report[@]}"

	check_if_safe ${report[@]}
	safe=$?

	if [[ $safe -gt 0 ]]; then
	#	echo "Dampening..."
	for (( d=0 ; ${d} < ${levels} ; d++ )); do
			if [[ ${d} -eq 0 ]]; then
				check_if_safe ${report[@]:1}
			else
				# This method of removing one element is ugly as hell and took way too long to get working.
				check_if_safe $( echo "${report[@]:0:${d}} ${report[@]:$(( $d + 1 ))}" )
			fi
			safe=$?
			if [ $safe -eq 0 ]; then
			       	echo "Level $d dampened successfully."
				safe_reports=$(( $safe_reports + 1 ))
				break
			fi
		done
	else
		safe_reports=$(( $safe_reports + 1 ))
	fi
	if [[ $safe -eq 0 ]]; then
		echo "SAFE"
	else
		echo "UNSAFE"
	fi

	echo Reports checked: $i
	echo Safe so far: $safe_reports
done

# The answer, the total number of safe reports after dampening
echo Total number of safe reports: $safe_reports
