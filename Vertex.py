class Vertex:
	def __init__(self, id:int, content='', summary=''):
		self.id = id
		self.content = content
		self.summary = summary
		self.adjacency = {}

	def alterSummary(self, summary):
		self.summary = summary
	
	def alterContent(self, content):
		self.content = content

	def getId(self):
		return self.id

	def getNeighbors(self):
		return self.adjacency.keys()

	def addNeighbor(self, neighbor, weight):
		self.adjacency[neighbor] = weight

	def delNeighbor(self, neighbor):
		if neighbor in self.adjacency.keys():
			del self.adjacency[neighbor]

	def getWeight(self, neighbor):
		if neighbor in self.adjacency.keys():
			return self.adjacency[neighbor]
		return -1

