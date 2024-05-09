class PrimsMST:
    def __init__(self, V, graph):
        self.V = V
        self.graph = graph

    def minKey(self, key, mstSet):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if mstSet[v] == False and key[v] < min_val:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        parent = [-1] * self.V
        key = [float('inf')] * self.V
        mstSet = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V - 1):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not mstSet[v] and self.graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = self.graph[u][v]

        print("\n\n\nPrim’s Minimum Spanning Tree:\nEdge \tWeight")
        minimumCost = 0
        for i in range(1, self.V):
            print(f"{parent[i]} -- {i} == {self.graph[i][parent[i]]}")
            minimumCost += self.graph[i][parent[i]]
        print(f"Minimum Cost: {minimumCost}")

class KruskalsMST:
    class Edge:
        def __init__(self, src, dest, weight):
            self.src = src
            self.dest = dest
            self.weight = weight

    class Subset:
        def __init__(self, parent, rank):
            self.parent = parent
            self.rank = rank

    def __init__(self, V, E, graph):
        self.V = V
        self.E = E
        self.graph = []
        i = 0
        for x in range(V):
            for y in range(x, V):
                if graph[x][y] != 0:
                    self.graph.append(self.Edge(x, y, graph[x][y]))
                    i += 1

    def find(self, subsets, i):
        if subsets[i].parent != i:
            subsets[i].parent = self.find(subsets, subsets[i].parent)
        return subsets[i].parent

    def union(self, subsets, x, y):
        xroot = self.find(subsets, x)
        yroot = self.find(subsets, y)

        if subsets[xroot].rank < subsets[yroot].rank:
            subsets[xroot].parent = yroot
        elif subsets[xroot].rank > subsets[yroot].rank:
            subsets[yroot].parent = xroot
        else:
            subsets[yroot].parent = xroot
            subsets[xroot].rank += 1

    def kruskalMST(self):
        result = []
        i = 0

        self.graph = sorted(self.graph, key=lambda item: item.weight)

        subsets = []
        for i in range(self.V):
            subsets.append(self.Subset(i, 0))

        e = 0
        i = 0
        while e < self.V - 1:
            next_edge = self.graph[i]
            i += 1

            x = self.find(subsets, next_edge.src)
            y = self.find(subsets, next_edge.dest)

            if x != y:
                e += 1
                result.append(next_edge)
                self.union(subsets, x, y)

        print("\n\n\nKruskal’s Minimum Spanning Tree:\nEdge \tWeight")
        minimumCost = 0
        for edge in result:
            print(f"{edge.src} -- {edge.dest} == {edge.weight}")
            minimumCost += edge.weight
        print(f"Minimum Cost: {minimumCost}")


if __name__ == "__main__":
    V = int(input("Enter the number of vertices in the graph: "))
    E = int(input("Enter the number of edges in the graph: "))

    graph = [[0] * V for _ in range(V)]
    for i in range(E):
        src, dest, weight = map(int, input(f"Enter edge {i+1} (source, destination, weight): ").split())
        graph[src][dest] = weight
        graph[dest][src] = weight

    primsMST = PrimsMST(V, graph)
    primsMST.primMST()

    kruskalsMST = KruskalsMST(V, E, graph)
    kruskalsMST.kruskalMST()



# Kruskal's algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph. Here's how it works:

# 1. Sort Edges by Weight: First, all the edges of the graph are sorted in ascending order based on their weights.

# 2. Select Edges: Starting with the edge of the lowest weight, Kruskal's algorithm iterates through the sorted list of edges.

# 3. Add Edges: For each edge, if adding it to the current set of edges does not create a cycle (i.e., it does not connect two vertices that are already in the same connected component), then the edge is added to the Minimum Spanning Tree.

# 4. Union-Find: To determine whether adding an edge will create a cycle, Kruskal's algorithm uses a data structure called a disjoint-set (or union-find) to keep track of the connected components. This data structure efficiently supports operations like finding the parent of a node and merging two sets.

# 5. Repeat: Kruskal's algorithm continues adding edges until there are \(|V| - 1\) edges in the MST, where \(|V|\) is the number of vertices in the graph.

# The time complexity of Kruskal's algorithm is \(O(E \log E + E \log V)\), where \(E\) is the number of edges and \(V\) is the number of vertices. This complexity arises from sorting the edges (\(O(E \log E)\)) and performing union-find operations (\(O(E \log V)\)).

# The space complexity of Kruskal's algorithm is \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. This space is primarily used for storing the graph and the data structures needed for union-find operations.


# Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph. Here's how it works:

# 1. Initialization: Start with an arbitrary vertex as the initial vertex of the MST.

# 2. Grow the MST: Repeat the following steps until all vertices are included in the MST:
#    - Select the vertex `v` with the minimum key value among the vertices not yet included in the MST.
#    - Add `v` to the MST.
#    - Update the key values of the vertices adjacent to `v`, if necessary.

# 3. Output: The resulting MST consists of the edges connecting the vertices in the MST.

# Prim's algorithm grows the MST one vertex at a time, always selecting the edge with the minimum weight that connects a vertex in the MST to a vertex outside the MST.

# Time Complexity: The time complexity of Prim's algorithm depends on the data structure used for the implementation. Using a priority queue (such as a binary heap or Fibonacci heap) to efficiently select the minimum key vertex, the time complexity is typically O(V log V + E), where V is the number of vertices and E is the number of edges. In dense graphs where E is close to V^2, Prim's algorithm can be optimized to have a time complexity of O(V^2) by using an adjacency matrix instead of a priority queue.

# Space Complexity: The space complexity of Prim's algorithm is O(V + E), where V is the number of vertices and E is the number of edges. This space is primarily used to store the graph and the data structures needed for bookkeeping during the algorithm's execution.

