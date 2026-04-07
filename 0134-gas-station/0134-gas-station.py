class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = curr = ans = 0 # curr act as current remaining tank capacity 
        for ind in range(len(gas)):
            diff = gas[ind] - cost[ind]
            tot += diff
            curr += diff
            if curr < 0:
                curr = 0
                ans = ind + 1

        return ans if tot >= 0 else -1

'''
Approach: Keep maintaining the total tank capacity since the start, and the tank capacity since the last start.
Update the current capacity to zero whenever it becomes negative and `ans` to the next index. If the total capacity
at the end is positive, it means the current answer fulfills the requirement.
'''
