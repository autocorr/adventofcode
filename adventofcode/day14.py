#!/usr/bin/env python3

from day10 import knot_hash


PUZZLE_INPUT = 'wenycdww'


def sum_bits(key):
    bits = 0
    for ii in range(128):
        kh = knot_hash('{0}-{1}'.format(key, ii))
        bits += sum(bin(int(c, 16)).count('1') for c in kh)
    return bits


def solve():
    print('-- sum of bits :', sum_bits(PUZZLE_INPUT))


