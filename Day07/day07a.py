#!/usr/bin/python3
###############################################################################
#
# 2024 Advent of Code, Day 07, Part 1
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
# The engineers need help determining which calibration equations can produce
# the given test values by inserting add (+) and multiply (*) operators between
# the numbers. The operators are evaluated left-to-right, and the numbers
# cannot be rearranged. Your task is to find the equations that could possibly
# be true and sum their test values to get the total calibration result.
#
# My Reflection:
# The hardest part of this day was figuring out how to generate a list of every
# combonation of the two operators. I wanted to write my own method rather than
# just look one up, and I ended up couting up an int, converting it to binary
# then replacing 0 or 1 with the operators. This took much trial and error to
# the point that I was commenting and uncommenting temporary output so many
# times that I altered my lazy level (up? down?) by using a debug boolean to
# suppress the output. Given a re-write I probably would use a command line 
# to control this rather than changing the variable in source.
#
# I knew this had to have been solved already somewhere in a python library
# that I hadn't learned yet, and I also wanted to see an AI solution, so after
# completing my version and getting the correct answer I asked ChatGPT to
# analyze my code and give an alternative solution. It did so quite well and
# suggested using product() in place of my binary conversion, which looked
# much clearner. I thus used this function in my part 2 code.
#
###############################################################################

import operator
import copy
import sys

debug = False

if (len(sys.argv) > 1):
    inputfile = sys.argv[1]
else:
    inputfile = "input"

lines = 0
total_calibration_result = 0

with open(inputfile,"r") as file:
    for line in file:
        answer = int( line.strip().split(":")[0] )
        equation = line.strip().split(":")[1].strip().split()

        num_figures = len(equation)
        num_operators = num_figures - 1
        if(debug): print("Figs: " + str(num_figures))
        if(debug): print("Ops: " + str(num_operators))

        # Use an int converted to binary and replace 0 and 1 with + and * to generate a full
        # list of every combonation of the operators.
        bin_len = num_operators
        if(debug): print("bin_len: " + str(bin_len))
        bin_num = "1" * bin_len
        if(debug): print("bin_num: " + str(bin_num))
        bin_num_dec = int(format(int(bin_num,2),"d"))
        if(debug): print("bin_num_dec: " + str(bin_num_dec))
        while(bin_num_dec >= 0):
            i_bin = format(bin_num_dec,"b").zfill(bin_len)
            if(debug): print("i_bin: " + str(i_bin))
            i_bin_replaced = i_bin.replace("0","+").replace("1","*")
            if(debug): print(i_bin_replaced)
            operators_list = list(i_bin_replaced).copy()
            if(debug): print(operators_list)

            j = 0
            solution = 0
            if(debug): print(equation)
            while(j < (num_operators)):
                if(debug): print(j)
                if ( j == 0 ):
                    filled_equation = ( str(equation[0]) + " " + str(operators_list[0]) + " " + str(equation[1]) )
                else:
                    filled_equation = ( str(solution) + " " + str(operators_list[j]) + " " + str(equation[j+1]) )
                if(debug): print(filled_equation)
                solution = eval(filled_equation)
                if(debug): print(solution)
                if(debug): print(equation[j])
                if(debug): print(str(equation) + " ?= " + str(answer) + " ?= " + str(solution))
                if ( answer == solution):
                    print("Found correct equation: " + str(equation) + " " + str(operators_list) + " = " + str(solution) + " = " + str(answer))
                    total_calibration_result = total_calibration_result + answer
                    print(total_calibration_result)
                    bin_num_dec = -1 #prevent another check
                    j = num_operators * 2 #prevent another check
                j = j + 1
            bin_num_dec = bin_num_dec - 1

        lines = lines + 1

print("Lines: " + str(lines))
print("Total calibration result: " + str(total_calibration_result))
