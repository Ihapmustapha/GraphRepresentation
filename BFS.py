from queue import Queue

from Graph import *


def breadth_first(graph,start=0,end=0):
    #putting starting vertex inside the queue
    queue = Queue()
    queue.put(start)

    #initializing visited array with ZEROS, we've not visited any vertext yet
    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        #while you didn't visit your destination yet then continue your search
        while visited[end] == 0:
            vertex = queue.get()
            #if you've visited this vertex before then skip it and go to another one
            if visited[vertex] == 1:
                 continue
            print('visit: ',vertex)
            visited[vertex] =1
            for v in graph.get_adjacent_vertices(vertex):
                #if the adjacent vertex is not visited then put it into the Queue
                if visited[v]!=1:
                    queue.put(v)


####################################################
##################~~Testing~~#######################
####################################################

g= AdjacencyMatrixGraph(9)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)

breadth_first(g, 2, 8)
