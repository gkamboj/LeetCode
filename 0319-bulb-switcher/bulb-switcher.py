class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)
    
    
# Approach: Observe that the final condition of a kth bulb will depend on the number of factors of k. Also, except for
# perfect squares, factors always occur in pair (for rg., 12 = 1 * 12 = 2 * 6 = 3 * 4) i.e. every number except
# perfect squares will always have even number of factors. If the bulb condition is changed even number of times,
# its final condition will be same as initial condition i.e. off. So, only those bulbs which are numbered perfect
# square numbers will be on at end as perfect squares have odd number of factors.

# PS: Number of perfect squares less than or equal to n = int(sqrt(n)).
