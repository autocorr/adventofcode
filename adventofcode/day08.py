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
    def __init__(self, name):
        self.name = name
        self.value = 0

    def __iadd__(self, n):
        self.value += n
        return self

    def __gt__(self, n):
        return self.value > n

    def __lt__(self, n):
        return self.value < n

    def __ge__(self, n):
        return self.value >= n

    def __le__(self, n):
        return self.value <= n

    def __eq__(self, n):
        return self.value == n

    def __neq__(self, n):
        return self.value != n


class Instruction:
    macro_fmt = 'if {cname} {op} {cval}: {tname} += {dval}'

    def __init__(self, line):
        params = line.split()
        self.tname = params[0] + '___'
        self.cname = params[4] + '___'
        sign = 1 if params[1] == 'inc' else -1
        self.macro = self.macro_fmt.format(
            cname=self.cname,
            op=params[5],
            cval=params[6],
            tname=self.tname,
            dval=sign*int(params[2]),
        )


class Cpu:
    def __init__(self, lines):
        self.max_value_held = 0
        self.instructions = [Instruction(l) for l in lines]
        self.registers = self.init_registers()
        self.execute()

    def init_registers(self):
        return {
            instr.tname: Register(instr.tname)
            for instr in self.instructions
        }

    def execute(self):
        locals().update(self.registers)
        for instr in self.instructions:
            exec(instr.macro)
            computed = self.registers[instr.tname].value
            if computed > self.max_value_held:
                self.max_value_held = computed

    def max(self):
        return max(reg.value for reg in self.registers.values())


def solve():
    with open('pi08.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    #lines = TEST_DATA.strip().split('\n')
    cpu = Cpu(lines)
    print('-- max value :', cpu.max())
    print('-- max held  :', cpu.max_value_held)


