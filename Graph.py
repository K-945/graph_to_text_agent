from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertex = 0
        self.numEdge = 0

    def getNumEdge(self):
        """ 获取图中边的数量

        :return:
        """
        return self.numEdge

    def getNumVertex(self):
        """ 获取图中顶点的数量

        :return:
        """
        return self.numVertex

    def addVertex(self, id, content='', summary=''):
        """ 添加顶点

        :param id: 顶点编号
        :param summary: 文本块摘要
        :param content: 文本块内容
        :return:
        """
        if id in self.vertexList.keys():
             raise ValueError("The id already exists in the graph, please re-create it.")
        self.numVertex += 1
        self.vertexList[id] = Vertex(id, content, summary)

    def getVertex(self, id):
        """ 获取指定编号的顶点的内容

        :param id: 目标顶点编号
        :return: 如果存在则返回内容，不存在则返回None
        """
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
        """ 添加边，如果输入的顶点有一个不存在就报错

        :param fromId: 起点
        :param toId: 终点
        :param weight: 边
        :return:
        """
        if fromId not in self.vertexList.keys() or toId not in self.vertexList.keys():
            raise ValueError("Both fromId and toId must already be created.")
        self.vertexList[fromId].addNeighbor(toId, weight)
        self.numEdge += 1

    def delEdge(self, fromId, toId):
        """ 删除指定两个结点之间的边

        :param fromId:起点
        :param toId: 终点
        :return:
        """
        if fromId not in self.vertexList.keys() or toId not in self.vertexList.keys():
            raise ValueError("Both fromId and toId must be created.")
        self.vertexList[fromId].addNeighbor(toId)
        self.numEdge -= 1

    def getWeight(self, fromId, toId):
        """ 获取两个顶点之间的权重，如果有则返回权重内容，没有则返回-1

        :param fromId: 起点
        :param toId: 终点
        :return: 权重
        """
        if fromId in self.vertexList.keys():
            if toId in self.vertexList[fromId].getNeighbors():
                return self.vertexList[fromId].getWeight(toId)
        return -1


