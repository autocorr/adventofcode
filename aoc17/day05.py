#!/usr/bin/env python3


def follow_jumps(ops, spooky=False):
    ops = ops.copy()
    address = 0
    counter = 0
    try:
        while True:
            offset = ops[address]
            ops[address] += -1 if spooky and offset >= 3 else 1
            address += offset
            counter += 1
    except IndexError:
        return counter


def solve():
    with open('pi05.txt', 'r') as f:
        ops = [int(s) for s in f.read().split()]
    print('-- number of jumps :', follow_jumps(ops))
    print('-- jumps if spooky :', follow_jumps(ops, spooky=True))


