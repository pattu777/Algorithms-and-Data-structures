#!/usr/bin/env python

# This is a adjacency list representation of a directed graph.

import sys

class Vertex(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Graph(object):
    def __init__(self, nodes=0):
        self.nodes = nodes
        self.arr = {}

    def add_edge(self, src, dest):
        self.arr[src].append(dest)

    def remove_edge(self, src, dest):
        for node in self.arr.keys():
            if self.arr

    def bfs(self):
        pass

    def dfs(self):
        pass
