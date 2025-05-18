class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[pos, sp] for pos, sp in zip(position, speed)]
        stack = []
        for pos, sp in sorted(arr, reverse=True):
            time = (target - pos) / sp
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)

# Approach: Check NeetCode solution at https://youtu.be/Pr6T-3yB9RM
