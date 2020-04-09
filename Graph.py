import numpy as np
import random as rd
from matplotlib import pyplot as plt

def generate_graph(n):
    
    #graph is represented by an adjacency list
    graph = {} #dictionnary = {vertex i : [list of neighbours]}
    
    for i in range(n):
        
        nb_neighbours = rd.randint(1,n-1) 
        possible_neighbours = [j for j in range(n) if j!=i] #we avoid having path from vertex i to vertex i
        neighbours = rd.sample(possible_neighbours, nb_neighbours)
        graph[i] = neighbours
    
    return graph

def Neighbours(graph, vertex):
    return graph[vertex]
    
def degree(graph, vertex):
    return len(Neighbours(graph, vertex))
    
def to_graph(paths,n):
    
    graphs = []
    
    for path in paths :
        
        initial_vertex = path[0]
        graph = {}
    
        for i in range(1,n) :
        
            next_vertex = path[i]
            graph[initial_vertex] = next_vertex
            initial_vertex = next_vertex
        
        graphs.append(graph)
    
    return graphs
        