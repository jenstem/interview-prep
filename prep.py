# Graph

# Adjancency List

class Graph:
    def __init__(self):
        self.adjacency_list = {}   

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True 
        return False


customDict = { "a" : ["b", "c", "d"],
               "b" : ["a", "e"],
               "c" : ["a", "d"],
               "d" : ["a", "c", "e"],
               "e" : ["b", "d"]}

graph = Graph(customDict)
graph.addVertex("e", "c")
print(graph.adjacency_list["e"])