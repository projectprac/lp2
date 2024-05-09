class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Assuming undirected graph

    def dijkstra(self, source):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[source] = 0
        visited = set()
        while len(visited) < len(self.graph):
            min_vertex = None
            min_distance = float('inf')
            for vertex, distance in distances.items():
                if vertex not in visited and distance < min_distance:
                    min_vertex = vertex
                    min_distance = distance
            visited.add(min_vertex)
            for neighbor, weight in self.graph[min_vertex].items():
                distance = distances[min_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
        return distances


def print_menu():
    print("\nMenu:")
    print("1. Add Edge")
    print("2. Find Shortest Distances from Source")
    print("3. Exit")


# Example usage:
g = Graph()

while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        u = input("Enter source vertex: ")
        v = input("Enter destination vertex: ")
        weight = float(input("Enter weight of the edge: "))
        g.add_edge(u, v, weight)
        print("Edge ({}, {}) with weight {} added.".format(u, v, weight))
    elif choice == '2':
        source = input("Enter the source vertex: ")
        shortest_distances = g.dijkstra(source)
        print("Shortest distances from source vertex", source, ":")
        for vertex, distance in shortest_distances.items():
            print("Vertex:", vertex, ", Distance:", distance)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
