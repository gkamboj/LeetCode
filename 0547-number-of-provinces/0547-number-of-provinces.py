class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
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
