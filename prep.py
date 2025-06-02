# Graph

# Graph Traversal - BFS

def bfs(self, vertex):
    visited = set()
    visited.add(vertex)
    queue = [vertex]
    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex)
        for adjacent_vertex in self.adjacency_list[current_vertex]:
            if adjacent_vertex not in visited:
                visited.add(adjacent_vertex)
                queue.append(adjacent_vertex)



