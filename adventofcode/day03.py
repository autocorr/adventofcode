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
#
# -> functions by "radius" R in straight lines
#   lower-right :  n = 4 * R**2 -  4 * R + 1
#   down        :  n = 4 * R**2 -  5 * R + 2
#   lower-left  :  n = 4 * R**2 -  6 * R + 3
#   left        :  n = 4 * R**2 -  7 * R + 4
#   upper-left  :  n = 4 * R**2 -  8 * R + 5
#   up          :  n = 4 * R**2 -  9 * R + 6
#   upper-right :  n = 4 * R**2 - 10 * R + 7
#   right       :  n = 4 * R**2 - 11 * R + 8
#
# The lower-right diagonal is the largest number before the radius increases.
# The manhatten distance to the center is symmetric by the four cardinal
# directions. Can use modulo 4 based on the number of values in an R to R+1
# interval.


PUZZLE_INPUT = 64

def solve():
    # radius -> solve lower-right, then round down
    # offset = (value - rad - 1) % 4
    # dist = radius + offset
    print('-- :', )


