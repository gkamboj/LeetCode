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
