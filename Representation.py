import numpy as np
from math import *
from matplotlib import pyplot as plt

def represent_vertex(ax, x, y):
    
    plt.scatter(x, y, color='red') 
    ax.annotate(str(x), (x,y+0.5) )

def represent_link(ax, x,y, x_neighbour, y_neighbour):

    dx = x_neighbour-x
    dy = y_neighbour-y
    ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.2, length_includes_head = True, fc='k')

def represent_graph(graph, n):
    
    fig, ax = plt.subplots()
    
    all_x = graph.keys()
    all_y = n*np.random.rand(n)

    for vertex in graph:
        
        x = vertex
        y = all_y[x]
        
        represent_vertex(ax, x, y)
        
        neighbours = Neighbours(graph, vertex)
        
        for neighbour in neighbours :
            
            x_neighbour, y_neighbour = neighbour, all_y[neighbour]
            represent_link(ax, x, y, x_neighbour, y_neighbour)
    
    plt.xlim(0,n)
    plt.ylim(0,n)

    plt.title('Graph')
    plt.savefig('Graph.png')
    plt.show()
    
    return all_x, all_y

def represent_paths(all_x, all_y, paths):
    
    m = len(paths)
    
    for i in range(m):
        
        fig, ax = plt.subplots()
        
        for x in all_x :
            
            y = all_y[x]
            represent_vertex(ax, x, y)
        
        path = paths[i]
        vertex_start = path[0]
        n = len(path)
        
        for j in range(1,n) :
            
            vertex = path[j]
            x = vertex_start
            y = all_y[x]
            x_neighbour = vertex
            y_neighbour = all_y[x_neighbour]
            represent_link(ax, x, y, x_neighbour, y_neighbour)
            vertex_start = vertex
    
        plt.xlim(0,n)
        plt.ylim(0,n)

        plt.title('Hamiltonian path number ' + str(i+1))
        plt.savefig("Hamiltonian_path_"+str(i+1)+".png")
    plt.show()