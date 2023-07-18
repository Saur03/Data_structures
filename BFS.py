# BFS is an algorithm to trace the nodes of the graph in a breadth-first order; that is the neighbouring nodes in a single-level are traversed first, then the nodes in the next level are traversed.

import collections
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # if not visited, mark it as visited, and
        # enqueue it

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '[__main__':
    graph = {0: [1.2], 1: [2], 2: [3], 3: [1,2]}
    print("BFS Travesal: ")
    bfs(graph,0)
