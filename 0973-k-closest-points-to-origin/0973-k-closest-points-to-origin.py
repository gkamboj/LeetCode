import heapq as h

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, dist_points = [], defaultdict(list)
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if not dist_points[dist]:
                h.heappush(heap, dist)
            dist_points[dist].append(point)
        ans = []
        while len(ans) < k:
            ans += dist_points[h.heappop(heap)]
        return ans
