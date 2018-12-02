#!/usr/bin/env python3

import numpy as np


TEST_INPUT = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


class Program:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None

    def __repr__(self):
        fmt = '<Program: {0} ({1}) [{2}]>'
        if self.children is not None:
            child_str = ' '.join(c.name for c in self.children)
        else:
            child_str = 'None'
        return fmt.format(self.name, self.weight, child_str)

    @staticmethod
    def from_str(line):
        # FIXME could use regex for better performance
        line = (line
            .replace('(', '')
            .replace(')', '')
            .replace(',', '')
        )
        if '->' in line:
            head, _, tail = line.partition('->')
            children = tail.split()
        else:
            head, children = line, None
        name, weight = head.split()
        return Program(name, int(weight), children)

    @property
    def siblings(self):
        return self.parent.children

    @property
    def tower_weight(self):
        if self.children is None:
            return self.weight
        else:
            return self.weight + sum(
                c.tower_weight for c in self.children
            )

    @property
    def which_unbalanced(self):
        weights = np.array([
            c.tower_weight for c in self.children
        ])
        if (weights == weights.max()).all():
            sib_w = [c.tower_weight for c in self.siblings]
            delta = max(sib_w) - min(sib_w)
            return self, self.weight - delta, sib_w
        else:
            return self.children[weights.argmax()].which_unbalanced


def link_programs(lines):
    name_map = {}
    for line in lines:
        prog = Program.from_str(line)
        name_map[prog.name] = prog
    for prog in name_map.values():
        if prog.children is not None:
            # link parent to children
            prog.children = [
                name_map[child_name]
                for child_name in prog.children
            ]
            # link children to parent
            for child in prog.children:
                child.parent = prog
    # find the root node
    while True:
        if prog.parent is None:
            return prog
        else:
            prog = prog.parent


def solve():
    with open('pi07.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    #lines = TEST_INPUT.strip().split('\n')
    root = link_programs(lines)
    print('-- root program :', root.name)
    print('-- unbalanced :', root.which_unbalanced)


