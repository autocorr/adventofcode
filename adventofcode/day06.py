#!/usr/bin/env python3

import numpy as np


PUZZLE_INPUT = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"


def parse_input(puzzle_input):
    return np.array(puzzle_input.split(), dtype=int)


def redistributed(banks):
    n_banks = len(banks)
    max_bank = banks.argmax()
    max_value = banks.max()
    banks[max_bank] = 0
    leftover = np.zeros(n_banks, dtype=int)
    leftover[:max_value % n_banks] = 1
    banks += np.roll(leftover, shift=max_bank+1) + max_value // n_banks


def processed_until_loop(banks):
    counter = 0
    previous_states = [tuple(banks)]
    while True:
        counter += 1
        redistributed(banks)
        state = tuple(banks)
        if state in previous_states:
            break
        else:
            previous_states.append(state)
    return counter


def solve():
    banks = parse_input(PUZZLE_INPUT)
    print('-- distributions before loop :', processed_until_loop(banks))
    print('-- distributions after loop  :', processed_until_loop(banks))


