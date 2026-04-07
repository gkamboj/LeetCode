class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = curr = ans = 0
        for ind in range(len(gas)):
            diff = gas[ind] - cost[ind]
            tot += diff
            curr += diff
            if curr < 0:
                curr = 0
                ans = ind + 1

        return ans if ans < len(gas) and tot >= 0 else -1
