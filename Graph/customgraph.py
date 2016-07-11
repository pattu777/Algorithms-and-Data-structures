# Adjacency list representation of a Graph.

class Vertex(object):
	def __init__(self, id):
		self.id = id

	def __eq__(self, vertex):
		return self.id == vertex.id

	def __str__(self):
		return str("Vertex-" + str(self.id))

class Edge(object):
	def __init__(self, src, dest, weight=0):
		self.src = src
		self.dest = dest
		self.weight = weight

	def __str__(self):
		return "Edge " + str(self.src) + " " + str(self.dest) + " Weight-" + str(self.weight)

class Graph(object):
	def __init__(self, size=0, is_directed=False):
		self.all_edges = []
		self.all_vertex = {}
		self.size = size
		self.is_directed = is_directed

	def add_edge(self, src, dest, weight=0):
		if src in self.all_vertex:
			src_vertex = self.all_vertex[src]
		else:
			src_vertex = Vertex(src)
			self.all_vertex[src] = src_vertex

		if dest in self.all_vertex:
			dest = self.all_vertex[dest]
		else:
			dest_vertex = Vertex(dest)
			self.all_vertex[dest] = dest_vertex

		edge = Edge(src_vertex, dest_vertex, weight)
		self.all_edges.append(edge)


if __name__ == '__main__':
	g = Graph(4, False)
	g.add_edge(1,2,10)
	g.add_edge(2,3,5)
	g.add_edge(1,4,6)

	for edge in g.all_edges:
		print(edge)

	for vertex in g.all_vertex:
		print("Vertex " + str(g.all_vertex[vertex]))
		for edge in g.all_vertex[vertex].edges:
			print("Edge " + str(edge))
		
