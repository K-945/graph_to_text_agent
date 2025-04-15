from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertex = 0
        self.numEdge = 0

    def getNumEdge(self):
        return self.numEdge

    def getNumVertex(self):
        return self.numVertex

    def addVertex(self, id, content='', summary=''):
        if id in self.vertexList.keys():
             raise ValueError("The id already exists in the graph, please re-create it.")
        self.numVertex += 1
        self.vertexList[id] = Vertex(id, content, summary)

    def getVertex(self, id):
        if id in self.vertexList:
            content = self.vertexList[id].content
            summary = self.vertexList[id].summary
            adjacency = self.vertexList[id].adjacency
            vertex_info = f"id:{id} summary:{summary} content:{content} adjacency:{adjacency}"
            # print(vertex_info)
            return self.vertexList[id]
        else:
            return None

    def getVertexes(self):
        vertexes_list = []
        for id in self.vertexList:
            vertexes_list.append(self.vertexList[id])
        return vertexes_list

    def addEdge(self, fromId, toId, weight):
        if fromId not in self.vertexList.keys() or toId not in self.vertexList.keys():
            raise ValueError("Both fromId and toId must already be created.")
        self.vertexList[fromId].addNeighbor(toId, weight)
        self.numEdge += 1

    def delEdge(self, fromId, toId):
        if fromId not in self.vertexList.keys() or toId not in self.vertexList.keys():
            raise ValueError("Both fromId and toId must be created.")
        self.vertexList[fromId].addNeighbor(toId)
        self.numEdge -= 1

    def getWeight(self, fromId, toId):
        if fromId in self.vertexList.keys():
            if toId in self.vertexList[fromId].getNeighbors():
                return self.vertexList[fromId].getWeight(toId)
        return -1


