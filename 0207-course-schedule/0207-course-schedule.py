class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        in_deg = defaultdict(int)

        for a, b in prerequisites:
            pre[b].append(a)
            in_deg[a] += 1
        
        queue = deque()
        for course in range(numCourses):
            if not in_deg[course]:
                queue.append(course)
        
        topo_sort = []
        while queue:
            curr = queue.popleft()
            topo_sort.append(curr)
            
            for node in pre[curr]:
                in_deg[node] -= 1
                if not in_deg[node]:
                    queue.append(node)
        
        return len(topo_sort) == numCourses
