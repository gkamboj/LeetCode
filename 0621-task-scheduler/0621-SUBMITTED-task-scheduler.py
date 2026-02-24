import heapq as h

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        
        ans, heap, q = 0, [-count for count in counter.values()], deque()
        h.heapify(heap)
        
        while heap or q:
            ans += 1
            if heap:
                count = h.heappop(heap) + 1
                if count:
                    q.append([count, ans + n])
            
            if q and q[0][1] == ans:
                h.heappush(heap, q.popleft()[0])
        
        return ans

# Approach: Refer NC video: https://youtu.be/s8p8ukTyA2I
