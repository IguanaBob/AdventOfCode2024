#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 05, Part 2
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
# After identifying the correctly-ordered updates, you now need to fix the
# incorrectly-ordered updates. For each of these, use the page ordering
# rules to arrange the page numbers in the correct order. Once you have the
# correct order for each update, find the middle page number, and sum these
# middle page numbers to get the final result for the incorrectly-ordered updates.
#
# My Reflection:
# So now we need to re-order bad updates to fix them. We do this by checking
# The rule list for valid updates and applying them by swapping the position
# of pages with a pop and insert of one of them.
#
###############################################################################

import re

def add_rule(new_rule):
    rules.append(line.strip().split("|"))
    return

def add_update(new_update):
    updates.append(new_update.strip().split(","))
    return

def check_update(update):
    for page in update:
        if ( update.count(page) > 1 ):
            return(1)
        for rule in rules:
            if ( rule[0] in update and rule[1] in update and page in rule):
                if ( update.index(rule[0]) > update.index(rule[1]) ):
                    return(1)
    return(0)

def fix_update(invalid_update):
    update = invalid_update.copy()
    print("Broken: " + str(update))
    while ( check_update(update) != 0 ):
        for page in update:
            for rule in rules:
                if ( rule[0] in update and rule[1] in update and page in rule):
                    if ( update.index(rule[0]) > update.index(rule[1]) ):
                        removed = update.pop(update.index(rule[1]))
                        update.insert(update.index(rule[0])+1,removed)
    print("Fixed: " + str(update))
    return(update.copy())

rules = []
updates = []
valid_updates = []
fixed_updates = []
middle_page_total = 0

with open("input","r") as file:
    for line in file:
        if ( "|"  in line.strip() ):
            add_rule(line.strip())
        elif ( "," in line.strip() ):
            add_update(line.strip())

for update in updates:
    if ( check_update(update) == 0 ):
        valid_updates.append(update)
    else:
        fixed_updates.append(fix_update(update).copy())

for fixed_update in fixed_updates:
    if ( len(fixed_update) % 2 == 1 ):
        middle_page = fixed_update[int(len(fixed_update)/2)]
        middle_page_total = middle_page_total + int(middle_page)

print("Valid updates: " + str(len(valid_updates)))
print("Fixed updates: " + str(len(fixed_updates)))
print("Total of middles of fixed: " + str(middle_page_total))
