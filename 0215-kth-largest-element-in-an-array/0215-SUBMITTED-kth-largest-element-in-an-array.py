import heapq as h

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                h.heappush(heap, num)
            elif heap[0] < num:
                h.heappop(heap)
                h.heappush(heap, num)
        return heap[0]

# Approach: Create min heap and keep adding till its size is k. After that, add (after popping
# curr min) whenever num is more than current min. This way, at last, we will have k largest numbers
# with kth largest at root.
