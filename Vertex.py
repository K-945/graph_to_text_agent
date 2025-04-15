class Vertex:
	def __init__(self, id:int, content='', summary=''):
		"""
		id：第几个文本块 \\
		summary：对文本块的凝练 \\
		content：原始文本块 \\
		adjacency：该文本块和其余哪些文本块有关系
		"""
		self.id = id
		self.content = content
		self.summary = summary
		self.adjacency = {}

	def alterSummary(self, summary):
		""" 修改凝练后的文本块内容
		"""
		self.summary = summary
	
	def alterContent(self, content):
		""" 修改文本块内容
		"""
		self.content = content

	def getId(self):
		""" 获取属于第几个文本块的信息
		"""
		return self.id

	def getNeighbors(self):
		""" 获取该文本块顶点和其余哪些文本块顶点之间有关联
		"""
		return self.adjacency.keys()

	def addNeighbor(self, neighbor, weight):
		""" 添加文本块顶点与文本块顶点之间的关系
		-----
		neighbor：尾顶点 \
		weight：关系信息
		"""
		self.adjacency[neighbor] = weight

	def delNeighbor(self, neighbor):
		""" 删除该文本块和另一个文本块之间的关联信息
		------
		neighbor：尾顶点
		"""
		if neighbor in self.adjacency.keys():
			del self.adjacency[neighbor]

	def getWeight(self, neighbor):
		""" 获取该文本块顶点和另一个指定文本块之间的关系，没有关系则输出为-1
		------
		neightbor：尾顶点
		"""
		if neighbor in self.adjacency.keys():
			return self.adjacency[neighbor]
		return -1

