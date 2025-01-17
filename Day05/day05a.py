#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 05, Part 1
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
# The North Pole printing department needs help ensuring that the pages
# for the sleigh launch safety manual updates are printed in the correct
# order. The page ordering rules specify which page must be printed before
# another. Your task is to identify which updates are in the correct order
# based on these rules, then find the middle page number of each correctly-ordered
# update and add them together to get the final result.
#
# My Reflection:
# Trying to use fuctions more. Nothing too difficult on this day.
#
###############################################################################

import re

def add_rule(new_rule):
    rules.append(line.strip().split("|"))
    #print("Rule number " + str(len(rules)) + ": Page #" + str(rules[len(rules)-1][0]) + " must come before page #" + str(rules[len(rules)-1][1]) )
    return

def add_update(new_update):
    if ( check_rules(new_update) == 0 ):
        updates.append(new_update.strip().split(","))
#    print("Valid Updates:")
#    for update in updates:
#        print(update)
    return

def find_middle(update):
#    print("Middle")
    return

def check_rules(line):
    valid = 0
    update = line.split(",")
#    print("Checking update: " + str(update))
    for page in update:
        if ( update.count(page) > 1 ):
#            print("Error: Page included in update more than once")
            return(1)
        for rule in rules:
            if ( rule[0] in update and rule[1] in update and page in rule):
                if ( update.index(rule[0]) > update.index(rule[1]) ):
#                    print("Rule violation: Rule:" + str(rule) + " Page:" + str(page))
                    return(1)
    valid_updates.append(update.copy())
    return(0)

rules = []
updates = []
valid_updates = []
middle_page_total = 0

with open("input","r") as file:
    for line in file:
        if ( "|"  in line.strip() ):
            add_rule(line.strip())
        elif ( "," in line.strip() ):
            add_update(line.strip())
#print("Valid updates: " + str(valid_updates))

for valid_update in valid_updates:
    # The input data contained updates with only an even number of pages so this check
    # is not strictly  necissary, I left it here to show my progress when writing this.
#    if ( len(valid_update) % 2 == 0 ):
        #print(str(valid_update) + " is Even: " + str(len(valid_update)))
    if ( len(valid_update) % 2 == 1 ):
        #print(str(valid_update) + " is Odd: " + str(len(valid_update)))
        middle_page = valid_update[int(len(valid_update)/2)]
        #print("Middle page is: " + str(middle_page))
        middle_page_total = middle_page_total + int(middle_page)

print(middle_page_total)
