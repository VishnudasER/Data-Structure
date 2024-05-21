class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))

# Sample workout 1: Undirected graph
graph1 = Graph()
graph1.add_edge(0, 1)
graph1.add_edge(0, 2)
graph1.add_edge(1, 2)
graph1.add_edge(2, 0)
graph1.add_edge(2, 3)
graph1.add_edge(3, 3)
print("Graph 1:")
graph1.print_graph()

# Sample workout 2: Directed graph
graph2 = Graph()
graph2.add_edge('A', 'B')
graph2.add_edge('A', 'C')
graph2.add_edge('B', 'C')
graph2.add_edge('C', 'A')
graph2.add_edge('C', 'D')
graph2.add_edge('D', 'D')
print("\nGraph 2:")
graph2.print_graph()

# Sample workout 3: Weighted graph
graph3 = Graph()
graph3.add_edge('A', ('B', 2))
graph3.add_edge('A', ('C', 3))
graph3.add_edge('B', ('C', 1))
graph3.add_edge('C', ('A', 4))
graph3.add_edge('C', ('D', 5))
graph3.add_edge('D', ('D', 6))
print("\nGraph 3:")
graph3.print_graph()


# Define a Graph class to represent the graph using an adjacency list
class Graph:
    def __init__(self):
        self.adj_list = {}

    # Add an edge to the graph
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    # Depth-first search traversal function
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        # Traverse all adjacent vertices of the current vertex
        if start in self.adj_list:
            for neighbor in self.adj_list[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

# Create a graph instance
g = Graph()

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform DFS traversal starting from vertex 2
print("DFS Traversal:")
g.dfs(0)
