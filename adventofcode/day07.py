#!/usr/bin/env python3


PUZZLE_INPUT = """
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

    @staticmethod
    def from_str(line):
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
    lines = PUZZLE_INPUT.strip().split('\n')
    root = link_programs(lines)
    print('-- root program :', root.name)


