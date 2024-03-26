class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos)/sp for (pos, sp) in sorted(zip(position, speed), reverse=True)]
        fleets, curr = 0, -1
        for time in times:
            if curr < time:
                curr = time
                fleets += 1
        return fleets
        