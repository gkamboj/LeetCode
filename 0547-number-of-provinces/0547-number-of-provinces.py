class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans, visited = 0, [False] * n
        
        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                ans += 1
                visited[i] = True
        
                while queue:
                    curr = queue.popleft()
                    for j in range(n):
                        if not visited[j] and isConnected[curr][j]:
                            queue.append(j)
                            visited[j] = True
        
        return ans

'''
Approach: BFS using given matrix
- Traverse all nodes, and for every unvisited node, run BFS, exploring all nodes reachable via direct or indirect connections.
- Each BFS traversal represents one connected component (province).

- Time Complexity: O(n²) (due to matrix traversal), 
- Space Complexity: O(n)
'''