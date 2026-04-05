class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, start, tank_capacity = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank_capacity += diff
            
            if tank_capacity < 0:
                start = i + 1
                tank_capacity = 0
        
        return start if total >= 0 else -1
            
        