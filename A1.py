from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def add_user_edge(self):
        while True:
            v = input("Enter the first vertex (or type 'stop' to finish adding edges): ")
            if v.lower() == "stop":
                break
            w = input("Enter the second vertex: ")
            self.add_edge(v, w)
            print(f"Edge ({v}, {w}) added successfully.")

    def dfs(self, v, d, visited=None):
        visited = visited or set()
        visited.add(v)
        print(v, end=" ")

        if v == d:
            return True

        for n in self.adj[v]:
            if n not in visited:
                if self.dfs(n, d, visited):
                    return True
        return False

    def bfs(self, s, d):
        visited = set()
        queue = deque()

        visited.add(s)
        queue.append(s)

        while queue:
            s = queue.popleft()
            print(s, end=" ")

            if s == d:
                return

            for n in self.adj[s]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

if __name__ == "__main__":
    g = Graph()

    while True:
        choice = input("\nEnter 1 to add a new edge, 2 for DFS traversal, 3 for BFS traversal, or any other key to exit: ")
        
        if choice == "1":
            g.add_user_edge()
        elif choice == "2":
            start = input("Enter the starting vertex for DFS traversal: ")
            end = input("Enter the target vertex for DFS traversal: ")
            print("Depth First Traversal:")
            g.dfs(start, end)
        elif choice == "3":
            start = input("Enter the starting vertex for BFS traversal: ")
            end = input("Enter the target vertex for BFS traversal: ")
            print("Breadth First Traversal:")
            g.bfs(start, end)
        else:
            print("Exiting...")
            break


# Breadth-First Search (BFS) is a fundamental graph traversal algorithm used in artificial intelligence (AI) and various other fields. It explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

# Application of BFS in AI:

# Shortest Path Finding: BFS can be used to find the shortest path between two nodes in an unweighted graph. In AI, this can be applied in pathfinding algorithms for tasks such as robot navigation or finding the shortest sequence of actions in a state space.

# Searching in State Space: In AI problem-solving, BFS can be used to explore states in a state space, especially when the transitions between states have uniform costs. This is particularly useful in applications like puzzle-solving (e.g., solving a Rubik's Cube or a maze) or planning problems.

# Web Crawling and Search Engines: BFS is utilized in web crawlers that systematically browse the internet by starting from a given webpage and exploring all linked webpages at the same level before moving deeper. This approach ensures that web pages are discovered efficiently and in a structured manner.

# Network Routing: BFS can be applied in network routing algorithms to find the shortest path between two nodes in a network. This is crucial in designing efficient communication networks where minimizing latency or maximizing throughput is essential.

# Game Theory and AI: In game theory, BFS can be used to explore the game tree to find optimal moves in games like chess or tic-tac-toe. By traversing the game tree level by level, BFS can help AI agents evaluate different possible moves and choose the one with the best outcome.

# Key Characteristics of BFS:


# FIFO Queue: BFS uses a FIFO (First-In-First-Out) queue to maintain the order in which nodes are explored. This ensures that nodes at the same level are explored before moving deeper into the graph.

# Complete and Optimal: When applied to finite graphs, BFS is complete (it will find a solution if one exists) and optimal (it will find the shortest path). However, in infinite graphs or graphs with cycles, BFS may not terminate.

# Memory Intensive: BFS requires memory to store the visited nodes and the queue of nodes to be explored, especially in graphs with many nodes or large branching factors.

# In summary, BFS is a versatile algorithm used in various AI applications for graph traversal, pathfinding, state space exploration, and network analysis. Its simplicity and efficiency make it a valuable tool in AI problem-solving and algorithm design.



# Depth-First Search (DFS) is another fundamental graph traversal algorithm used in artificial intelligence (AI) and various other fields. Unlike Breadth-First Search (BFS), which explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level, DFS explores as far as possible along each branch before backtracking.


# Application of DFS in AI:

# State Space Search: DFS is commonly used in AI for state space search problems, such as puzzle-solving (e.g., solving a Rubik's Cube or a maze) and planning problems. It explores possible states recursively, often leading to a more memory-efficient implementation compared to BFS.

# Graph Traversal: DFS is useful for traversing graphs, particularly in applications like finding connected components, detecting cycles, and determining reachability between nodes.

# Topological Sorting: DFS can be employed to perform topological sorting, which is essential in scheduling tasks with dependencies, such as job scheduling or course planning.

# Maze Solving and Pathfinding: In maze-solving problems, DFS can be used to explore the maze until it finds a solution, often resulting in a depth-first exploration of the maze's paths.

# Game Tree Search: In game theory and AI, DFS can be applied to traverse game trees to find optimal moves in games like chess or tic-tac-toe.

# Key Characteristics of DFS:

# Backtracking: DFS explores as far as possible along each branch before backtracking. This characteristic makes it well-suited for problems where a solution might be found deep in the search tree.

# Stack-based Implementation: DFS is often implemented using a stack data structure to keep track of the nodes to visit. This allows for the recursive nature of the algorithm.

# Incomplete and Non-optimal: Unlike BFS, DFS is not complete or optimal in general. It may get stuck in infinite loops or return suboptimal solutions depending on the problem and the search space.

# Memory Efficiency: DFS tends to use less memory compared to BFS because it explores one branch of the search tree as deeply as possible before backtracking, which reduces the memory overhead of maintaining the search frontier.

# In summary, DFS is a versatile algorithm used in various AI applications for state space search, graph traversal, topological sorting, maze solving, and game tree search. Its ability to explore deeply into a search space and its memory efficiency make it an essential tool in AI problem-solving and algorithm design.
