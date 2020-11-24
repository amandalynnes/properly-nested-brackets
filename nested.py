#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: My program reads a file, tests it, and writes results.
"""

__author__ = "Amanda Simmons, JT"

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
    for char in line:
        stack.append(char)
    print(stack)


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt', 'r') as f:
        for line in f:
            is_nested(line.strip())


if __name__ == '__main__':
    main(sys.argv[1:])
