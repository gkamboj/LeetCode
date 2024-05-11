class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map[key]
        if not vals or vals[0][0] > timestamp:
            return ''
        start, end = 0, len(vals) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid + 1
        return vals[end][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

'''
Approach: Store vales in dictionary: both timestamp and value. While getting, use binary search. Handle return
statement edge case.
'''
