#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: My program reads a file, tests it, and writes results.
"""

__author__ = "Amanda Simmons, JT, Pete Mayor"

import sys

# read input.txt file
# print to terminal and write results to output.txt file
# check if all brackets in input.txt file are nested properly
# possibly store example brackets in a dictionary/ list?
# use a list as a stack
# look up the shunting yard algorithm


def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []
# (  )
# [  ]
# {  }
# <  >
# (*  *)
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>', '(*': '*)'}
    # print(brackets)
    index = 0
    print(line)
    while index < len(line):
        # print(index)
        if (index == len(line) - 1):
            if line[index] in brackets:
                stack.append(line[index])
            break
        next_two_char = line[index] + line[index+1]
        # print(next_two_char)
        if (next_two_char in brackets):
            index += 1
            stack.append(next_two_char)
        elif (line[index] in brackets):
            stack.append(line[index])
        if stack:
            last_in_stack = stack[-1]
            if (next_two_char == brackets[last_in_stack]):
                index += 1
                stack.pop()
            elif (line[index] == brackets[last_in_stack]):
                stack.pop()
            elif next_two_char in brackets.values() or line[index] in brackets.values():
                print(f'NO, {index}')
                return

        elif next_two_char in brackets.values() or line[index] in brackets.values():
            print(f'NO, {index}')
            return
        index += 1
    if stack:
        print(f'NO, {index}')
    else:
        print('YES')
    # print(stack)
# plan for stack- look at last char of the stack.
# if that char is a matching opening to the current char
# remove the last char in the stack
# if all of the brackets match up the stack should be empty


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open(args[0], 'r') as f:
        for line in f:
            is_nested(line.strip())


if __name__ == '__main__':
    main(sys.argv[1:])
