#!/usr/bin/env python3
# -> Spiral as ccw
#
#   65 64 63 62 61 60 59 58 57
#   66 37 36 35 34 33 32 31 56
#   67 38 17 16 15 14 13 30 55
#   68 39 18 05 04 03 12 29 54
#   69 40 19 06 01 02 11 28 53
#   70 41 20 07 08 09 10 27 52
#   71 42 21 22 23 24 25 26 51
#   72 43 44 45 46 47 48 49 50
#   73 74 75 76 77 78 79 80 81
#                4  5  6  7  8
#
# -> lower-right diagonal increases as square:
#   R = (2 * n + 1)**2
#   n = (sqrt(R) - 1) / 2
#
# The manhatten distance to the center is symmetric by
# the four cardinal directions.
# After googling the first few terms, the solution to the second
# part can be found on OEIS:
#     https://oeis.org/A141481/b141481.txt

import numpy as np


def manhattan_distance(N):
    R = int((np.sqrt(N) - 1) / 2) + 1
    n_hi = (2 * R + 1)**2
    n_lo = (2 * (R - 1) + 1)**2
    perim = np.arange(n_lo + 1, n_hi + 1)
    cards = R + n_lo + (np.arange(4) * (n_hi - n_lo)) // 4
    offset = min(abs(cards - N))
    return offset + R


def solve():
    #N = 64
    N = 325489
    print('-- manhattan distance :', manhattan_distance(N))


