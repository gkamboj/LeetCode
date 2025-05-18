class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos)/sp for (pos, sp) in sorted(zip(position, speed), reverse=True)]
        ans, curr = 0, 0
        for time in times:
            if curr < time:
                curr = time
                ans += 1
        return ans