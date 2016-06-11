# This is an adjacency matrix representation of a Graph.

from Queue import Queue

class Graph(object):
	def __init__(self, vertex=0):
		self.vertex = vertex
		self.arr = [[0 for i in xrange(self.vertex)] for x in xrange(self.vertex)]

	def add_edge(self, src, dest):
		"""Add an edge to the Graph."""
		self.arr[src][dest] = 1

	def remove_edge(self, src, dest):
		"""Remove an edge from the Graph."""
		self.arr[src][dest] = 0

	def bfs(self):
		"""Perform breadth first search on a Graph."""
		pass

	def count_edges(self):
		"""Count the total number of edges in a Graph."""
		edge_count = 0
		for x in xrange(self.vertex):
			for y in xrange(self.vertex):
				if self.arr[x][y] == 1:
					edge_count += 1

		return edge_count

	def count_vertex(self):
		"""Return the number of vertices of a Graph."""
		return self.vertex
