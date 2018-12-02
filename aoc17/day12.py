#!/usr/bin/env python3

import re


def parse_input(filen='pi12.txt'):
    graph = {}
    with open(filen, 'r') as f:
        for line in f:
            node, *edges = re.findall(r'\d+', line)
            graph[node] = edges
    return graph


def remove_connected(graph, to_visit):
    connected = set()
    while to_visit:
        node = to_visit.pop()
        if node in graph:
            edges = graph.pop(node)
            to_visit.extend(edges)
        connected.update({node})
    return connected


def solve():
    graph = parse_input()
    root = '0'
    groups = {}
    groups[root] = remove_connected(graph, graph.pop(root))
    while graph:
        node, edges = graph.popitem()
        groups[node] = remove_connected(graph, edges)
    print('-- connected to root :', len(groups[root]))
    print('-- number of groups  :', len(groups))


