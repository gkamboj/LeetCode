class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0:
            return -1

        start = tot = -1
        c_start = c_tot = -1
        for ind, val in enumerate(delta):
            c_tot = max(val, c_tot + val)
            if c_tot >= 0 and c_start < 0:
                c_start = ind
            elif c_tot < 0:
                start = tot = -1
                c_start = c_tot = -1
            if c_tot > tot:
                tot = c_tot
                start = c_start
        
        return start