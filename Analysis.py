import numpy as np
from Graph import *

def mean_degree(graph, n):
    
    m = 0
    
    for vertex in graph :
        m += degree(graph, vertex)
    
    return m/n

def min_degree(graph, n):
    
    min = inf
    
    for vertex in graph :
        d = degree(graph,vertex)
        if  d < min:
            
            min = d
    return min

def not_already_visited(neighbours, path):
    
    next_vertices = []
    
    for neighbour in neighbours :
        
        visited = False
        
        for visited_vertex in path :
        
            if visited_vertex == neighbour :
        
                visited = True
                break
        
        if not visited :
            
            next_vertices.append(neighbour)
    
    return next_vertices
    
def all_hamiltonian_paths(graph, n, x, y):

    pathnext = [[x]]
    hamiltonian_paths = []

    while len(pathnext) > 0:
        
        path = pathnext.pop() # current path 
        m = len(path)
        vertex = path[m-1] # last visited vertex
        
        if vertex == y : 
            #if the vertex is y
            
            if m==n :
                #if all vertices have been visited
                #then it is an hamiltonian path
                hamiltonian_paths.append(path)
            
            #otherwise forget about the path
        
        else :
            #path can be completed
            neighbours = Neighbours(graph, vertex)
            next_vertices = not_already_visited(neighbours, path)
            
            for vertex in next_vertices :
                #all neighbours not already visited create a new path
                new_path = path + [vertex]
                pathnext.append(new_path)
    
    return hamiltonian_paths    