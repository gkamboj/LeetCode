class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage[key]
        start, end = 0, len(values) - 1
        ans_ind, ans = -1, ''
        while start <= end:
            mid = start + (end - start) // 2
            val, ts = values[mid][0], values[mid][1]
            if ts == timestamp:
                return values[mid][0]
            elif ts < timestamp:
                if mid > ans_ind:
                    ans_ind = mid
                    ans = values[ans_ind][0]
                start = mid + 1
            else:
                end = mid - 1
        return ans


        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)