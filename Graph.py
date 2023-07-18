#implementation of graph and it is a mathematical concept and graph is consist of edges and vertices
# created class graph and called init method or constructor and pass edges and vertices
class Graph:
    # Constructor or inot method
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        self.adjList = [[] for _ in range(n)]
        # add edges to the directed graph
        for (src,dest) in edges:
            self.adjList[src].append(dest)

# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        #print current vertex and all its neigboring vertices
        for dest in graph.adjList[src]:
            print(f'({src} -> {dest}) ', end= ' ')
        print()    

if __name__=='__main__':

    #Input: Edges in a directed graph
    edges = [(0,1), (1,2), (2,0), (2,1), (3,2), (4,5), (5,4) ]

    # No. of vertices (labelled from 0 to 5)
    n = 6

    # construct a graph from a given list of edges
    graph = Graph(edges, n)
 
    # print adjacency list representation of the graph
    printGraph(graph)
    
     
