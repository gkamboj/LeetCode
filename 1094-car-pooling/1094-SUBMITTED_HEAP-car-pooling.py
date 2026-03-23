class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        heap, tot = [], 0

        for (num, frm, to) in trips:
            while heap and heap[0][0] <= frm:
                _, count = heapq.heappop(heap)
                tot -= count
            heapq.heappush(heap, (to, num))
            tot += num
            if tot > capacity:
                return False
        
        return True

'''
Approach: Similar to LC-253 (Meeting Rooms II), maintain a min heap to the current minimum end time as well as the capacity
of the trip with that time. For every new trip, if the start time is after the minimum end time of the heap, remove it from the heap
and subtract the capacity from the total till now.
If the total surpasses the input max capacity at any point, return False.
'''
