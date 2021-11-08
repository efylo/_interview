from collections import defaultdict
from random import shuffle


class Graph:
    """implementation of graph data structure, using adjacency list representation"""
    def __init__(self, ):
        self.graph = defaultdict(list)
        # additional attributes possible
        # self.directed = True
        # self.weighted = False
       
    def connect(self, u, v):
        # if graph undirected need one more line
        self.graph[u].append(v)

    # BFS starting from a node
    def BFS(self, node, visited = defaultdict(bool)):
        q = [node]
        visited[node] = True
        # loop till no nodes are left
        while not not q:
            node = q.pop(0)
            print(node, end = "  ")
            for adjacent in self.graph[node]:
                if not visited[adjacent]:
                    q.append(adjacent)
                    visited[adjacent] = True
    
    def BFSAll(self, ):
        visited = defaultdict(bool)
        nodes = list(self.graph.keys())
        shuffle(nodes)

        for node in nodes:
            if not visited[node]:
                self.BFS(node, visited)
        print("")

    # DFS starting from a node
    def DFS(self, node, visited=defaultdict(bool)):
        print(node, end="  ")
        visited[node] = True
        for adjacent in self.graph[node]:
            if not visited[adjacent]:
                self.DFS(adjacent, visited)
    
    def DFSAll(self, ):
        visited = defaultdict(bool)
        nodes = list(self.graph.keys())
        shuffle(nodes)

        for node in nodes:
            if not visited[node]:
                self.DFS(node, visited)
        print("")



# directed graph
g = Graph()

g.connect(0, 1)
g.connect(0, 2) # g.graph[0] = [1, 2]
g.connect(1, 2) # g.graph[1] = [2]
g.connect(2, 0)
g.connect(2, 3) # g.graph[2] = [0, 3]
g.connect(3, 3) # g.graph[3] = [3]

g.BFSAll() # BFS for all nodes, even there is isolated graph
g.DFSAll() # DFS ..
