#!/usr/bin/env python3

import numpy as np


def parse_dance(filen):
    with open('pi16.txt', 'r') as f:
        ops = f.read().strip().split(',')
    moves = []
    for op in ops:
        code = op[0]
        data = op[1:]
        if code == 's':
            value = int(data)
        elif code == 'x':
            i, j = data.split('/')
            i, j = int(i), int(j)
            value = (i, j)
        elif code == 'p':
            a, b = data.split('/')
            a = int(a, 32) - 10
            b = int(b, 32) - 10
            value = (a, b)
        else:
            raise ValueError('Invalid move "{0}"'.format(move))
        moves.append((code, value))
    return moves


def apply_dance(group, moves):
    for code, v in moves:
        if code == 's':
            group[:] = np.roll(group, v)
        elif code == 'x':
            group[v[0]], group[v[1]] = group[v[1]], group[v[0]]
        else:
            i = np.argmax(group == v[0])
            j = np.argmax(group == v[1])
            group[i], group[j] = group[j], group[i]


def dancers(group):
    return ''.join(chr(n+97) for n in group)


def solve():
    moves = parse_dance('pi16.txt')
    group = np.arange(16)
    apply_dance(group, moves)
    print('-- order after dance :', dancers(group))
    repeats_after = 60  # from testing
    for _ in range(int(1e9-1) % repeats_after):
        apply_dance(group, moves)
    print('-- and after one billion dances :', dancers(group))


