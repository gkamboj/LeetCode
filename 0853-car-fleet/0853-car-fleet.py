class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans, time = 0, -1
        arr = [[pos, sp] for pos, sp in zip(position, speed)]
        for pos, sp in sorted(arr, reverse=True):
            currTime = (target - pos)/sp
            if currTime > time:
                time = currTime
                ans += 1
        return ans