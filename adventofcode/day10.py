#!/usr/bin/env python3

import numpy as np


PUZZLE_INPUT = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'


def hashed_sparse(ring, offsets, trials=1):
    size = len(ring)
    pos, skip = 0, 0
    for _ in range(trials):
        for offset in offsets:
            ix = np.arange(pos, pos+offset) % size
            ring[ix] = ring[ix][::-1]
            pos = (pos + offset + skip) % size
            skip += 1


def dense_hash(ring):
    xored = [
        np.bitwise_xor.reduce(ring[i*16:(i+1)*16])
        for i in range(16)
    ]
    return ''.join('{0:0>2x}'.format(i) for i in xored)


def solve_first():
    ring = np.arange(256)
    offsets = np.array(PUZZLE_INPUT.split(','), dtype=int)
    hashed_sparse(ring, offsets)
    print('-- product 1 & 2 :', ring[0]*ring[1])


def solve_second():
    ring = np.arange(256)
    suffix = [17, 31, 73, 47, 23]
    offsets = np.array([ord(c) for c in PUZZLE_INPUT]+suffix)
    hashed_sparse(ring, offsets, trials=64)
    print('-- knot hash :', dense_hash(ring))


def solve():
    solve_first()
    solve_second()


