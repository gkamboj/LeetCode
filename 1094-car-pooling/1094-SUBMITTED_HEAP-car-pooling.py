class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        heap, tot = [], 0
        print(trips)
        for (num, frm, to) in trips:
            while heap and heap[0][0] <= frm:
                _, count = heapq.heappop(heap)
                print(count)
                tot -= count
            heapq.heappush(heap, (to, num))
            tot += num
            if tot > capacity:
                return False
        
        return True
