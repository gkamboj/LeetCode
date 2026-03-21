"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key = lambda x:x.start)
        for val in intervals:
            if heap and heap[0] <= val.start:
                heapq.heappop(heap)
            heapq.heappush(heap, val.end)
        return len(heap)

'''
Approach: 
- Heap stores the end times of meetings currently occupying rooms.
- Smallest end time is always at the top, representing the room that frees up the earliest.
- If the earliest-ending meeting finishes before the current one starts, we can reuse that room by popping the current minimum from heap.
- Else, we must allocate a new room.
'''
