import numpy as np
from Graph import *

def mean_degree(graph, n):
    
    """Computes the mean degree of each vertex of the graph"""
    
    # sum of the degree of each vertex
    m = 0
    for vertex in graph :
        m += degree(graph, vertex)
    
    # Divide by the number of vertices to obtain the mean 
    return m/n

def min_degree(graph, n):
    
    """Computes the minimum degree of a vertex in the graph"""
    
    # initialize with +infinite
    min = inf
    
    for vertex in graph :
        
        # for each vertex of the graph
        d = degree(graph,vertex)
        
        if  d < min:
            # if its degree is lower
            # then it's the new minimum
            min = d
    
    return min

def not_already_visited(neighbours, path):
    
    """Return the list of neighours not already visited in the path"""
    
    # List of vertices that can be added to our path 
    next_vertices = []
    
    for neighbour in neighbours :
        #for each neighbour of our vertex
        #Let's check if it has already been visited
        
        visited = False
        
        for visited_vertex in path :
            # comparing this neighbour with each vertex previously added to the path 
            if visited_vertex == neighbour :
                # if it has been visited, stop comparing
                # don't add it to next_vertices list
                visited = True
                break
        
        if not visited :
            # otherwise add it to next_vertices list
            next_vertices.append(neighbour)
    
    return next_vertices
    
def all_hamiltonian_paths(graph, n, x, y):
    
    """Return all Hamiltonian paths in the graph"""
    
    # Stack of compatible paths from x
    pathnext = [[x]]

    #List of Hamiltonian paths found
    hamiltonian_paths = []

    while len(pathnext) > 0:
        # while the stack is not empty
        # while all possibilities have not been foreseen
        
        # unstack the last path built
        path = pathnext.pop() 
        # take its length
        m = len(path)
        # take its last vertex 
        vertex = path[m-1] 
        
        if vertex == y : 
            # if this vertex is y
            # we have a path between x and y
            
            if m==n :
                # if all vertices have been visited
                # then it is a Hamiltonian path
                hamiltonian_paths.append(path)
            
            # otherwise it is not a Hamiltonian path
        
        else :
            # path can be completed
            
            # The vertices that can be added from the last vertex mussn't have already appeared in the graph 
            neighbours = Neighbours(graph, vertex)
            next_vertices = not_already_visited(neighbours, path)
            
            for vertex in next_vertices :
                # all neighbours not already visited create a new possible path
                new_path = path + [vertex]
                
                # path added to our stack
                pathnext.append(new_path)
    
    return hamiltonian_paths    