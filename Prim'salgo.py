# Prim's minimal Spanning Tree algorithm
# A tree is a graph of vertices and edges without a cycle
# A spanning tree has all vertices connected and is constructed from the graph, and a graph can have multiple spanning trees.
# A minimal spanning tree is a spanning tree whose sum of weights of edges is the minimum 

INF = 9999999
# No of vertices in graph
V = 5
# 2 D array with 5X5 dimensions is created
# for adjacency matrix to represent graph
G = [[0, 19, 5, 0, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

# We need array to track vertex that selects 
# selected will be true else it will be false
selected = [0, 0, 0, 0, 0]     
# always set number of edges to zero
no_edge = 0
# If V = vertex then edge will be V -1 in MST
# choose 0th vertex and make it true
selected[0] = True
# print edge and weight
print(" Edge : Weight\n")
while (no_edge < V - 1):
    minimum = INF
    a = 0
    b = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        a = i
                        b = j
            print(str(a) + "-" + str (b) + ":" + str(G[a][b])) 
            selected[b] = True
            no_edge += 1   