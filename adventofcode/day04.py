#!/usr/bin/env python3

import numpy as np


PUZZLE_INPUT = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc aaa
"""


def parse_input(puzzle_input):
    return [
        line.split()
        for line in puzzle_input.strip().split('\n')
    ]


def valid_passphrase(phrase):
    return len(phrase) == len(np.unique(phrase))


def solve():
    phrases = parse_input(PUZZLE_INPUT)
    good_phrases = sum(valid_passphrase(phrase) for phrase in phrases)
    print('-- total phrases :', len(phrases))
    print('-- good phrases  :', good_phrases)


