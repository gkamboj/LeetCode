class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = defaultdict(int)
        for (num, frm, to) in trips:
            events[frm] += num
            events[to]-= num
        
        curr = 0
        for event in sorted(events.keys()):
            curr += events[event]
            if curr > capacity:
                return False
        
        return True

'''
Approach: Same as sweep line array, just using a dictionary instead of an array.
Using a dictionary reduces space complexity if not all times are covered from 1 to 1000, but needs extra sorting time.

Consider every pickup and drop as an event: with pickup time adding the passenger at that point of time,
and drop time subtracting those passengers. Now, if at any time the number of passengers surpasses capacity, polling
can't be done. If there's no such time, pooling is possible.
'''
