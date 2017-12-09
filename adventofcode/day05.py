#!/usr/bin/env python3


PUZZLE_INPUT = "0 3 0 1 -3"


def follow_jumps(ops):
    ops = ops.copy()
    address = 0
    counter = 0
    try:
        while True:
            offset = ops[address]
            ops[address] += 1
            address += offset
            counter += 1
    except IndexError:
        return counter


def solve():
    ops = [int(s) for s in PUZZLE_INPUT.split()]
    print('-- number of jumps :', follow_jumps(ops))


