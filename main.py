import Graph
import Representation
import Analysis
import random as rd

# Number of vertices
n = 50

# Generate random graph
graph = generate_graph(n)

# information about its density
# print(mean_degree(graph, n))
# print(min_degree(graph, n))

# Represent generated graph
all_x, all_y = represent_graph(graph, n)

# Generate Random vertices x and y
x = rd.randint(0,n-1)
y = rd.randint(0,n-1)

# Search for Hamiltonian paths between x and y

if x == y:
    
    # A Hamiltonian paths is between two different vertices 
    print("x and y have same value : No path")

else :
    
    # Generate all Hamiltonian paths
    paths = all_hamiltonian_paths(graph, n, x, y)
    
    if len(paths) == 0:
        
        # there might be no Hamiltonian paths between x and y 
        print("no hamiltonian_paths between "+ str(x) + " and " + str(y))
    
    else :
        
        # if there exists Hamiltonian paths between x and y
        # show x and y
        print(x, y)
        
        # Represent all Hamiltonian paths
        represent_paths(all_x, all_y, paths, n)
        
        #Show Hamiltonian paths
        print(to_graph(paths,n))