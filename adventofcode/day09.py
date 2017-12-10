#!/usr/bin/env python3


def cancel(stream):
    cancelled = False
    for s in stream:
        if cancelled:
            cancelled = False
            continue
        elif s == '!':
            cancelled = True
            continue
        else:
            yield s


def collect(stream):
    collecting = False
    for s in stream:
        if collecting:
            if s == '>':
                collecting = False
            continue
        elif s == '<':
            collecting = True
            continue
        else:
            yield s


def count_score(stream):
    frame, score = 0, 0
    for s in stream:
        if s == '{':
            frame += 1
        elif s == '}':
            score += frame
            frame -= 1
    return score


def count_garbage(stream):
    total = 0
    collecting = False
    for s in stream:
        if collecting:
            if s == '>':
                collecting = False
            else:
                total += 1
            continue
        elif s == '<':
            collecting = True
    return total


def solve():
    with open('pi09.txt', 'r') as f:
        stream = f.read().strip()
    #stream = '<{o"i!a,<{i<a>'
    print('-- curly score :', count_score(collect(cancel(stream))))
    print('-- total garbage :', count_garbage(cancel(stream)))


