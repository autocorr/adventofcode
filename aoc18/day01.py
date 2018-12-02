#!/usr/bin/env python3
import numpy as np


def solve():
    with open('pi01.txt') as f:
        numbers = np.loadtxt(f, dtype=int)
    frequency = numbers.cumsum()[-1]
    print(f'-- Resulting frequency: {frequency}')
