#import numpy to setup the matrix
import  numpy as np
#import Abstract
import abc


########################################################
#
# The Base class representation of a Graph with all of
# the interface methods
#
########################################################

class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        #no of Vertices in the graph
        self.numVertices = numVertices
        #is it directed or not
        self.directed = directed

    # Edges inside the graph: Links between vertices
    #
    # Define the method as an abstract method, 'pass' must be added to notify that the method is an
    # abstraction which could be used by importing the class Graph
    #
    #method's arguments: V1 and V2-> the two Vertices, weight-> weight/cost between those two Vertices
    @abc.abstractclassmethod
    def add_edge(self, v1, v2, weight):
        pass

    #get adjacent vertices of a specific vertex in the graph
    @abc.abstractclassmethod
    def get_adjacent_vertices(self, v):
        pass

    #get degree of a vertex
    @abc.abstractclassmethod
    def get_indegree(self, v):
        pass

    #get edge weight between two specific vertices
    @abc.abstractclassmethod
    def get_edge_weight(self, v1, v2):
        pass

    #display the graph
    @abc.abstractclassmethod
    def display(self):
        pass



######################################################################
#
# Represents a graph as an adjacency matrix. A cell in the matrix has
# a value when there exists an edge between the vertex represented by
# the row and column numbers.
# Weighted graphs can hold values > 1 in the matrix cells
# A value of 0 in the cell indicates that there's no edge
#
######################################################################

class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        #initialization for all matrix cells = zero
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        #Handling Errors of Vertices Values
        if v1 >= self.numVertices or v2 >= self.numVertices or v1<0 or v2<0:
            raise ValueError('Vertices %d and %d are out of bounds' %(v1,v2))

        #Handling Minus Weights
        if weight <1:
            raise ValueError('An Edge cannot have weight <1')

        #settig the weight from v1 to v2
        self.matrix[v1][v2] = weight

        #and if it's not a directed graph then weight from v2 to v1 is the same
        if self.directed == False:
            self.matrix[v2][v1] = weight

    #get Adjacent vertices of a single vertex
    def get_adjacent_vertices(self, v):
        #Handling wrong value of a vertex
        if v < 0 or v >= self.numVertices :
            raise ValueError('Cannot access vertex %d' %v)
        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return  adjacent_vertices


    #Getting degree of a vertex (no of connected nodes to a specific vertex)
    def get_indegree(self, v):
        #Handling wrong value of a vertex
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertex %d' % v)

        #initialize the degree = 0
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                indegree = indegree + 1

        return  indegree

    #Get weight of an edge
    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]


    #display the graph
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i,"-->",v)


###########################################################
########################--Testing--########################
###########################################################


g = AdjacencyMatrixGraph(4)

g.add_edge(0,1,50)
g.add_edge(0,2,20)
g.add_edge(2,3,34)

for i in range(4):
            print("Adjacent to ", i, g.get_adjacent_vertices(i))

for i in range(4):
            print("Indegree: ", i, g.get_indegree(i))

for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge Weight: ", i, " ", j, " weight", g.get_edge_weight(i,j))

g.display()
