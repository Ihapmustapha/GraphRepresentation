from Graph import *


def depth_first(graph, start=0, end=1):

    
    stack = list()

    stack = [(start, [start])]
    while stack:
        (node,path) = stack.pop()
        for next in (set(graph.get_adjacent_vertices(node))-set(path)):
            if next == end:
                print("possible path:", path + [next])
            else:
                stack.append((next, path + [next]))


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

visited = np.zeros(g.numVertices)
depth_first(g,0,5)