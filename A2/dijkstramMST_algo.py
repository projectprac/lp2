import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def addEdge(self, nodeA, nodeB, weight):
        if nodeA not in self.graph:
            self.graph[nodeA] = []
        self.graph[nodeA].append((nodeB, weight))

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_val = sys.maxsize
        min_index = -1
        for u in range(self.V):
            if dist[u] < min_val and not sptSet[u]:
                min_val = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            if u in self.graph:
                for v, w in self.graph[u]:
                    if not sptSet[v] and dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w

        self.printSolution(dist)

# Driver's code
if __name__ == "__main__":
    V = int(input("Enter the number of vertices in the graph: "))
    g = Graph(V)

    E = int(input("Enter the number of edges in the graph: "))
    print("Enter the edges in the format 'NodeA NodeB Weight':")
    for _ in range(E):
        nodeA, nodeB, weight = map(int, input().split())
        g.addEdge(nodeA, nodeB, weight)
        g.addEdge(nodeB, nodeA, weight)  # Assuming undirected graph

    start_node = int(input("Enter the starting node: "))
    g.dijkstra(start_node)
