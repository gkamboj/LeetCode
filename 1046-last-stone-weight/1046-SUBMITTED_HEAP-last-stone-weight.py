import heapq as h

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stone for stone in stones]
        h.heapify(heap)
        while len(heap) > 1:
            s1, s2 = h.heappop(heap), h.heappop(heap)
            h.heappush(heap, s1 - s2)
        return abs(heap[0])
