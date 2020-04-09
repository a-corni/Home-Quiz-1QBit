import numpy as np
import random as rd
from matplotlib import pyplot as plt

def generate_graph(n):
    
    """Return a random graph of n vertices"""
    
    #graph is represented by an adjacency list
    graph = {} #dictionnary = {vertex i : [list of neighbours]}
    
    for i in range(n):
        # Each vertex
        # has more than one neighbour and less than n-1 neighbour
        nb_neighbours = rd.randint(1,n-1) 
        
        # we forbid a vertex beeing its own neighbour
        possible_neighbours = [j for j in range(n) if j!=i]
        
        # list of neighbours
        # defined by taking nb_neighbours out of the whole set of neighbours 
        neighbours = rd.sample(possible_neighbours, nb_neighbours)
        graph[i] = neighbours
    
    return graph

def Neighbours(graph, vertex):
    
    """Return the neighbours of the vertex in the graph"""
    
    return graph[vertex]
    
def degree(graph, vertex):
    
    """Return the degree of the vertex in the graph"""
    
    # degree of a vertex is the number of its neighbours
    
    return len(Neighbours(graph, vertex))
    
def to_graph(paths,n):
    
    """Convert the list of Hamiltonian paths as defined in all_hamiltonian_paths into a list of graph representing these paths""" 
     
    # list of graphs
    graphs = []
    
    for path in paths :
        
        # for each Hamiltonian path defined in all_hamiltonian_paths as a list
        # we will define a new graph
        graph = {}
        
        # initialize with the first vertex of the path
        initial_vertex = path[0]
        
        for i in range(1,n) :
        
            # each next vertex of the path
            next_vertex = path[i]
            # is defined as the only neighbour of the current vertex 
            graph[initial_vertex] = [next_vertex]
            # next vertex becomes current vertex 
            initial_vertex = next_vertex
        
        #store the new graph into the list of graphs
        graphs.append(graph)
    
    return graphs