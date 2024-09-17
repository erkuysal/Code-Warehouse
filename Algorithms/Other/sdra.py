# Weekly Contest 409.Q2
# Shortest Distance After Road Addition Queries

class Solution():
    def shortest_distance_aq(self, n, queries):
        """
            :type n: int
            :type queries: List[List[int]]
            :rtype: List[int]
        """
        # Initialize the graph with the basic path from i to i+1
        graph = [[] for _ in range(n)]

        for i in range(n - 1):
            graph[i].append(i + 1)

        def bfs():
            # BFS to find the shortest path from 0 to n-1
            dist = [-1] * n
            dist[0] = 0
            queue = [0]  # Start BFS from node 0
            front = 0

            while front < len(queue):
                node = queue[front]
                front += 1

                for neighbor in graph[node]:
                    if dist[neighbor] == -1:  # If the neighbor has not been visited
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
                        if neighbor == n - 1:
                            return dist[n - 1]  # Early exit if we reach node n-1

            return dist[n - 1]

        # Processing each query
        answer = []
        for u, v in queries:
            graph[u].append(v)
            answer.append(bfs())

        return answer


# Example Usage:
n = 5
queries = [[0, 3], [3, 4], [1, 4]]
result = Solution().shortest_distance_aq(n, queries)
print(result)  # Expected output: [2, 2, 2]
