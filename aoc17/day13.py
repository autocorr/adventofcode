#!/usr/bin/env python3


class Layer:
    def __init__(self, depth, cells):
        self.depth = depth
        self.cells = cells

    def pos(self, delay=0):
        x = delay + self.depth
        per = 2 * (self.cells - 1)
        return abs(((x - per / 2) % per) - per / 2)

    @property
    def severity(self):
        return self.depth * self.cells


class FireWall:
    def __init__(self, filen):
        self.layers, self.max_depth = self.parse(filen)

    @staticmethod
    def parse(filen):
        layers = {}
        with open(filen, 'r') as f:
            for line in f:
                depth, cells = line.split(': ')
                depth = int(depth)
                cells = int(cells)
                layers[depth] = Layer(depth, cells)
        return layers, depth

    def run(self):
        severity = 0
        for layer in self.layers.values():
            if layer.pos() == 0:
                severity += layer.severity
        return severity

    def caught(self, delay=0):
        for layer in self.layers.values():
            if layer.pos(delay) == 0:
                return True
        return False


def solve():
    fw = FireWall('pi13.txt')
    print('-- severity :', fw.run())
    delay = 0
    while fw.caught(delay):
        delay += 1
    print('-- minimum delay :', delay)


