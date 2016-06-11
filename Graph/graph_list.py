#!/usr/bin/env python

# This is a adjacency list representation of a directed graph.

import sys

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data

class Graph(object):
    def __init__(self, nodes=0):
        """A dictionary of vertices and edges."""
        self.nodes = {}

    def nodes(self):
        """Returns all the nodes of the graph"""
        return self.nodes.keys()

    def edges(self):
        """Returns all the edges of a graph"""
        edges = []
        for node in self.nodes:
            for incident in self.nodes[node]:
                edge = (node, incident)
                if edge not in edges:
                    edges.append(edge)
        return edges

    def add_edge(self, src, dest):
        """Insert a new edge."""
        node = Node(src)
        self.nodes[node] = [x]
        self.nodes[x].append(node)

    def remove_edge(self, node):
        """Removes a given node  of the graph"""
        for node in self.nodes:
            if node in self.nodes[node]:
                self.nodes[node].remove(node)
        del self.nodes[node]

    def print_graph(self):
        pass

