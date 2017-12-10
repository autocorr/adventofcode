#!/usr/bin/env python3

from collections import deque


def cancel(stream):
    cancelling = False
    for c in stream:
        if cancelling:
            cancelling = False
            continue
        elif c == '!':
            cancelling = True
            continue
        else:
            yield c


def collect(stream):
    collecting = False
    for c in stream:
        if collecting:
            if c == '>':
                collecting = False
            continue
        elif c == '<':
            collecting = True
            continue
        else:
            yield c


def count_score(stream):
    depth, score = 0, 0
    for c in stream:
        if c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
    return score


def count_garbage(stream):
    total, collecting = 0, False
    for c in stream:
        if collecting:
            if c == '>':
                collecting = False
            else:
                total += 1
            continue
        elif c == '<':
            collecting = True
    return total


def stack_solution(string):
    stack = deque(string)
    score, depth, garbage, collecting = 0, 0, 0, False
    while stack:
        c = stack.popleft()
        if c == '!':
            stack.popleft()
        elif collecting and c != '>':
            garbage += 1
        elif c == '<':
            collecting = True
        elif c == '>':
            collecting = False
        elif c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
    return score, garbage


def solve():
    with open('pi09.txt', 'r') as f:
        stream = f.read().strip()
    #stream = '<{o"i!a,<{i<a>'
    score = count_score(collect(cancel(stream)))
    garbage = count_garbage(cancel(stream))
    print('-- iter based :', score, garbage)
    print('-- stack based :', *stack_solution(stream))


