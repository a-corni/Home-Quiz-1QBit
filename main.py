import Graph
import Representation
import Analysis
import random as rd

n = 8

graph = generate_graph(n)

all_x, all_y = represent_graph(graph, n)

x = rd.randint(0,n-1)
y = rd.randint(0,n-1)

if x == y:
   
    print("x and y have same value : No paths")

else :

    paths = all_hamiltonian_paths(graph, n, x, y)
    
    if len(paths) == 0:
     
        print("no hamiltonian_paths between "+ str(x) + " and " + str(y))
    
    else :
    
        print(x, y)
        represent_paths(all_x, all_y, paths)
        print(to_graph(paths,n))