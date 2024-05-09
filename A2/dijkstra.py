import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # For undirected graph

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist

def input_graph():
    V = int(input("Enter the number of vertices in the graph: "))
    g = Graph(V)
    print("Enter the edges (source, destination, weight):")
    while True:
        edge = input("Enter edge (or press Enter to stop): ").strip()
        if not edge:
            break
        u, v, w = map(int, edge.split())
        if u < 0 or u >= V or v < 0 or v >= V:
            print("Error: Invalid vertex number. Vertex number should be between 0 and", V-1)
            continue
        g.add_edge(u, v, w)
    return g

def display_menu():
    print("\nMenu:")
    print("1. Input graph")
    print("2. Find Shortest Distances from Source Vertex")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = display_menu()

        if choice == '1':
            g = input_graph()
        elif choice == '2':
            if 'g' not in locals():
                print("Error: Graph not yet inputted.")
                continue
            source = int(input("Enter source vertex: "))
            distances = g.dijkstra(source)
            print("Shortest distances from source vertex", source)
            for i, distance in enumerate(distances):
                print("Vertex", i, ":", distance)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
