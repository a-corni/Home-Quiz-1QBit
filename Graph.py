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
