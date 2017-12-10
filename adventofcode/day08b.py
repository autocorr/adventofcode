#!/usr/bin/env python3
# This a more standard solution without abusing the runtime.

import operator


TEST_DATA = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


class Register:
    def __init__(self):
        self.v = 0


class Instruction:
    op_map = {
        '>':  operator.gt,
        '<':  operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
    }

    def __init__(self, line):
        params = line.split()
        sign = 1 if params[1] == 'inc' else -1
        self.tname = params[0]
        self.cname = params[4]
        self.op = self.op_map[params[5]]
        self.cval = int(params[6])
        self.dval = sign*int(params[2])

    def compute(self, registers):
        treg = registers[self.tname]
        creg = registers[self.cname]
        if self.op(creg.v, self.cval):
            treg.v += self.dval
        return treg.v


class Cpu:
    def __init__(self, lines):
        self.max_value_held = 0
        self.instructions = [Instruction(l) for l in lines]
        self.registers = {
            instr.tname: Register()
            for instr in self.instructions
        }
        self.execute()

    def execute(self):
        for instr in self.instructions:
            result = instr.compute(self.registers)
            if result > self.max_value_held:
                self.max_value_held = result

    def max(self):
        return max(reg.v for reg in self.registers.values())


def solve():
    with open('pi08.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    #lines = TEST_DATA.strip().split('\n')
    cpu = Cpu(lines)
    print('-- max value :', cpu.max())
    print('-- max held  :', cpu.max_value_held)


