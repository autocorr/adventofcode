#!/usr/bin/env python3

from collections import Counter
import numpy as np


def parse_input(puzzle_input):
    return [
        line.split()
        for line in puzzle_input.strip().split('\n')
    ]


def validate_unique(phrase):
    return len(phrase) == len(np.unique(phrase))


def validate_anagram(phrase):
    words = [Counter(w) for w in phrase]
    while words:
        w = words.pop()
        if w in words:
            return False
    else:
        return True


def solve():
    with open('pi04.txt', 'r') as f:
        phrases = parse_input(f.read())
    unique_phrases = sum(validate_unique(phrase) for phrase in phrases)
    nonanagram_phrases = sum(validate_anagram(phrase) for phrase in phrases)
    print('-- total phrases :', len(phrases))
    print('-- unique phrases :', unique_phrases)
    print('-- non-anagram phrases :', nonanagram_phrases)


