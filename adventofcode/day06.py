#!/usr/bin/env python3

import numpy as np


PUZZLE_INPUT = "0 2 7 0"


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


def process_until_loop(banks):
    banks = banks.copy()
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
    print('-- distributions before loop :', process_until_loop(banks))


