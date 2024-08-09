
def depth_first_search(data_graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  # Print the current node

    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(data_graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


# Perform DFS starting from node 'A'
print("DFS traversal starting from node 'A':")
depth_first_search(graph, 'A')
