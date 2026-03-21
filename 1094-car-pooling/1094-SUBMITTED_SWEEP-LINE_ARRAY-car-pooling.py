class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [0 for i in range(1001)]
        for (num, frm, to) in trips:
            events[frm] += num
            events[to]-= num
        
        curr = 0
        for event in events:
            curr += event
            if curr > capacity:
                return False
        
        return True

'''
Approach: Consider every pickup and drop as an event: with pickup time adding the passenger at that point of time,
and drop time subtracting those passengers. Now, if at any time the number of passengers surpasses capacity, polling
can't be done. If there's no such time, pooling is possible.
'''
