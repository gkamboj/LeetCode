class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map[key]
        if not vals:
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
        return '' if end < 0 else vals[end][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)