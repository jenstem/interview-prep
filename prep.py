# Graph

# Graph Traversal - BFS

from collections import deque

class Graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_list = {}
        self.adjacency_matrix = adjacency_matrix
        self.visited = [False] * len(adjacency_matrix)
        self.discovery_time = [0] * len(adjacency_matrix)
        self.finishing_time = [0] * len(adjacency_matrix)
        self.time = 0   

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() or vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)   

    def dfs(self, vertex):
        self.visited[vertex] = True
        self.time += 1
        self.discovery_time[vertex] = self.time
        print(f"Vertex {vertex} discovered at time {self.discovery_time[vertex]}") 

        for adjacent_vertex in range(len(self.adjacency_matrix[vertex])):
            if self.adjacency_matrix[vertex][adjacent_vertex] == 1 and not self.visited[adjacent_vertex]:
                self.dfs(adjacent_vertex)
        self.time += 1
        self.finishing_time[vertex] = self.time
        print(f"Vertex {vertex} finished at time {self.finishing_time[vertex]}")        


adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

custom_graph = Graph(adjacency_matrix)
custom_graph.dfs(0)