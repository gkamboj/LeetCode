import heapq as h

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            if len(heap) < k:
                h.heappush(heap, [-(point[0] ** 2 + point[1] ** 2), point])
            elif abs(heap[0][0]) > point[0] ** 2 + point[1] ** 2:
                h.heappop(heap)
                h.heappush(heap, [-(point[0] ** 2 + point[1] ** 2), point])
        return [point[1] for point in heap]    
            