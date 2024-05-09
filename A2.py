from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.H = {}

    def add_edge(self, v, w, weight):
        self.adj[v].append((w, weight))
        self.adj[w].append((v, weight))

    def add_user_edge(self):
        while True:
            v = input("Enter the first vertex (or type 'stop' to finish adding edges): ")
            if v.lower() == "stop":
                break
            w = input("Enter the second vertex: ")
            weight = int(input("Enter the weight of the edge: "))
            self.add_edge(v, w, weight)
            print(f"Edge ({v}, {w}) with weight {weight} added successfully.")

    def h(self, v):
        return self.H.get(v, float('inf'))

    def a_star_algorithm(self, s, d):
        open_list = [(0, s)]
        closed_list = set()
        g = {s: 0}
        parent = {s: s}

        while open_list:
            _, n = heappop(open_list)

            if n == d:
                reconst_path = []
                while parent[n] != n:
                    reconst_path.append(n)
                    n = parent[n]
                reconst_path.append(n)
                reconst_path.reverse()
                print("Path found:", reconst_path)
                return

            for v, weight in self.adj[n]:
                if v not in closed_list and v not in (node[1] for node in open_list):
                    heappush(open_list, (g[n] + weight + self.h(v), v))
                    parent[v] = n
                    g[v] = g[n] + weight
                elif g[v] > g[n] + weight:
                    parent[v] = n
                    g[v] = g[n] + weight
                    if v in closed_list:
                        closed_list.remove(v)
                        heappush(open_list, (g[v] + self.h(v), v))
            closed_list.add(n)

        print("Path does not exist!")

if __name__ == "__main__":
    graph = Graph()

    while True:
        choice = input("\nEnter 1 to add a new edge, 2 for A* algorithm, or any other key to exit: ")
        
        if choice == "1":
            graph.add_user_edge()
        elif choice == "2":
            start = input("Enter the starting vertex: ")
            end = input("Enter the target vertex: ")
            print("Running A* algorithm...")
            graph.a_star_algorithm(start, end)
        else:
            print("Exiting...")
            break





# What is A* Search Algorithm? 

# A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

# What A* Search Algorithm does is that at each step it picks the node according to a value-‘f’ which is a parameter equal to the sum of two other parameters – ‘g’ and ‘h’. At each step it picks the node/cell having the lowest ‘f’, and process that node/cell.

# We define ‘g’ and ‘h’ as simply as possible below

# g = the movement cost to move from the starting point to a given square on the grid, following the path generated to get there. 

# h = the estimated movement cost to move from that given square on the grid to the final destination. This is often referred to as the heuristic, which is nothing but a kind of smart guess. We really don’t know the actual distance until we find the path, because all sorts of things can be in the way (walls, water, etc.). There can be many ways to calculate this ‘h’ which are discussed in the later sections.



# Algorithm 

# We create two lists – Open List and Closed List (just like Dijkstra Algorithm)  

# // A* Search Algorithm

# 1.  Initialize the open list

# 2.  Initialize the closed list
#     put the starting node on the open 
#     list (you can leave its f at zero)

# 3.  while the open list is not empty

#     a) find the node with the least f on 
#        the open list, call it "q"

#     b) pop q off the open list
  
#     c) generate q's 8 successors and set their 
#        parents to q
   
#     d) for each successor
#         i) if successor is the goal, stop search
        
#         ii) else, compute both g and h for successor

#           successor.g = q.g + distance between successor and q

#           successor.h = distance from goal to successor 
          
#           successor.f = successor.g + successor.h

#         iii) if a node with the same position as 
#             successor is in the OPEN list which has a 
#            lower f than successor, skip this successor

#         iV) if a node with the same position as 
#             successor  is in the CLOSED list which has
#             a lower f than successor, skip this successor
#             otherwise, add  the node to the open list

#      end (for loop)
  
#     e) push q on the closed list
#     end (while loop)