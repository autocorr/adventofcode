#!/usr/bin/env python3
# NOTE this method would make a lot more sense in Racket! The use of
# metapgrogramming with `locals` and `eval` is likely a poor solution
# because it is totally opaque what `eval(instr.macro)` does.


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
    macro_fmt = 'if creg.v {op} {cval}: treg.v += {dval}'

    def __init__(self, line):
        params = line.split()
        self.tname = params[0]
        self.cname = params[4]
        sign = 1 if params[1] == 'inc' else -1
        self.macro = self.macro_fmt.format(
            cname=self.cname,
            op=params[5],
            cval=params[6],
            tname=self.tname,
            dval=sign*int(params[2]),
        )

    def compute(self, regs):
        treg = regs[self.tname]
        creg = regs[self.cname]
        exec(self.macro)
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


