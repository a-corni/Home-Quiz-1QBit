import numpy as np
from math import *
from matplotlib import pyplot as plt

def represent_vertex(ax, x, y):
    
    """Plot a vertex at position x, y on the figure ax"""
    
    # Draw a red dot at position x, y
    plt.scatter(x, y, color='red')
    # Write vertex name above it
    ax.annotate(str(x), (x,y+0.5) )

def represent_link(ax, x,y, x_neighbour, y_neighbour):
    
    """Plot an array between vertex (x, y) and its neighbour (x_neighbour, y_neighbour) on the figure ax"""
    
    dx = x_neighbour-x
    dy = y_neighbour-y
    # Draw a black arrow between (x, y) and (x+dx, y+dy)
    ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.2, length_includes_head = True, fc='k')

def represent_graph(graph, n):
    """Represent initial graph, return its graphical representation"""
    
    fig, ax = plt.subplots()
    
    # Graphical representation : 
    # each vertex define the absciss
    all_x = graph.keys()
    # ordinate is a random number between 0 and n 
    all_y = n*np.random.rand(n)

    for vertex in graph:
        # for each vertex in the graph
        # get its coordinate 
        x = vertex
        y = all_y[x]
        
        # represent it
        represent_vertex(ax, x, y)
        
        # get its neighbours
        neighbours = Neighbours(graph, vertex)
        
        for neighbour in neighbours :
            # for each neighbour of the vertex
            # draw an array from the vertex to its neighbour
            x_neighbour, y_neighbour = neighbour, all_y[neighbour]
            represent_link(ax, x, y, x_neighbour, y_neighbour)
    
    # Definition of the window
    plt.xlim(0,n)
    plt.ylim(0,n)
    plt.title('Graph')
    
    # Save the picture in Graph.png
    plt.savefig('Graph.png')
    plt.show()
    
    #return the graphical representation used
    return all_x, all_y

def represent_paths(all_x, all_y, paths, n):
    
    """Plot all the different Hamiltonian paths of the graph""" 
    
    # Number of Hamiltonian paths 
    m = len(paths)
    
    for i in range(m):
        # for each Hamiltonian path
        path = paths[i]
        
        # define the figure on which we will plot the path 
        fig, ax = plt.subplots()
        
        # draw the vertices of the initial graph 
        for x in all_x :
            
            y = all_y[x]
            represent_vertex(ax, x, y)
        
        # draw the edges
        # take the first vertex (random vertex x)
        vertex_start = path[0]
        
        for j in range(1,n) :
            # for each vertex following x
            vertex = path[j]
            
            # draw an array between the former vertex and the new one
            # coordinate of the former vertex
            x = vertex_start
            y = all_y[x]
            # coordinate of the vertex
            x_neighbour = vertex
            y_neighbour = all_y[x_neighbour]
            # link them by an array
            represent_link(ax, x, y, x_neighbour, y_neighbour)
            vertex_start = vertex
        
        # Define the window
        plt.xlim(0,n)
        plt.ylim(0,n)
        plt.title('Hamiltonian path number ' + str(i+1))
        
        # Save the result in a png file
        plt.savefig("Hamiltonian_path_"+str(i+1)+".png")
    
    #Show all paths
    plt.show()