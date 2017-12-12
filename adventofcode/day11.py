#!/usr/bin/env python3


class Cell:
    dir_map = {
        'n':  ( 0,  1, -1),
        'ne': ( 1,  0, -1),
        'se': ( 1, -1,  0),
        's':  ( 0, -1,  1),
        'sw': (-1,  0,  1),
        'nw': (-1,  1,  0),
    }

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.furthest = 0

    def move_towards(self, direction):
        dx, dy, dz = self.dir_map[direction]
        self.x += dx
        self.y += dy
        self.z += dz
        if self.origin_dist > self.furthest:
            self.furthest = self.origin_dist

    @property
    def origin_dist(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) // 2


def solve():
    with open('pi11.txt', 'r') as f:
        steps = f.read().strip().split(',')
    walker = Cell()
    for s in steps:
        walker.move_towards(s)
    print('-- steps away :', walker.origin_dist)
    print('-- furthest   :', walker.furthest)


