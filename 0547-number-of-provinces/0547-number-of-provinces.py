class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans, visited = 0, [0 for i in range(n)]
        
        for i in range(n):
            if not visited[i]:
                stack = [i]
                ans += 1
                visited[i] = 1 
        
                while stack:
                    curr = stack.pop()
                    for j in range(n):
                        if not visited[j] and isConnected[curr][j]:
                            stack.append(j)
                            visited[j] = 1
        
        return ans

'''
Approach: DFS using given matrix
- For each unvisited node, we run DFS (using stack) to explore all directly and indirectly connected nodes.
- Each DFS traversal corresponds to one connected component (province).

- Time Complexity: O(n²) (due to matrix traversal), 
- Space Complexity: O(n)
'''