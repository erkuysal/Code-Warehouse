# Graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}


# Breadth First Search traversal function
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex, end=' ')  # Print the current vertex

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# Perform BFS traversal starting from vertex 0
print("BFS traversal starting from vertex:")
bfs(graph, 0)