# DFS is an algorithm to trace the nodes of the graph in a depth-first order; the nodes in one depth are traversed first, then the nodes in a paralled depth are traversed. It uses the concept of back-tracking sfter one vertical depth node is traversed.
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
graph = {'0': set(['1','2']),
          '1': set(['0', '1', '2']),   
          '2': set(['0']),
          '3': set(['1']),
          '4': set(['2', '3'])}

dfs(graph, '0')                      