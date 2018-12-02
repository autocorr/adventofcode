#!/usr/bin/env python3


def generator(seed, factor, align=None):
    key = 2147483647
    value = seed
    if align is None:
        while True:
            value = (value * factor) % key
            yield value
    else:
        while True:
            value = (value * factor) % key
            if not value % align:
                yield value


def judge_digits(x, y):
    return (x % 65536) == (y % 65536)


def solve_one():
    gen_a = generator(116, 16807)
    gen_b = generator(299, 48271)
    score = 0
    for _ in range(int(4e7)):
        if judge_digits(next(gen_a), next(gen_b)):
            score += 1
    print('-- judged score :', score)


def solve_two():
    gen_a = generator(116, 16807, 4)
    gen_b = generator(299, 48271, 8)
    score = 0
    for _ in range(int(5e6)):
        if judge_digits(next(gen_a), next(gen_b)):
            score += 1
    print('-- aligned judged score :', score)


def solve():
    solve_one()
    solve_two()


