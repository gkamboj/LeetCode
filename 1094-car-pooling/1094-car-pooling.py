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
