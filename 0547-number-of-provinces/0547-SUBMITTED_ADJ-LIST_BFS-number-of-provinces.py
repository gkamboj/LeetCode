class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        ans, visited = 0, [0 for i in range(n)]
        
        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                ans += 1
                visited[i] = 1 
        
                while queue:
                    curr = queue.popleft()
                    for node in graph[curr]:
                        if not visited[node]:
                            queue.append(node)
                            visited[node] = 1
        
        return ans

'''
Approach: BFS using adjacency list
- Convert the given adjacency matrix into an undirected adjacency list, ensuring each edge is added once (using j = i+1) but in both directions.
- Traverse all nodes, and for every unvisited node, run BFS to mark all reachable nodes.
- Each BFS traversal represents one connected component (province).

- Time Complexity: O(n²) (due to matrix traversal), 
- Space Complexity: O(n²) (adj list in dense graph).
'''
