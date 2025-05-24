class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]
        if not values or values[0][1] > timestamp:
            return ""
        ans = values[0]
        start, end = 0, len(values) - 1
        while start <= end:
            mid = start + (end - start) // 2
            mid_ts = values[mid][1]
            if mid_ts == timestamp:
                return values[mid][0]
            elif mid_ts < timestamp:
                if mid_ts > ans[1]:
                    ans = values[mid]
                start = mid + 1
            else:
                end = mid - 1
        return ans[0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)