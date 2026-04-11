class Solution: 
    def lexicalOrder(self, n: int) -> List[int]:
        curr, result = 1, []
        for _ in range(n):
            result.append(curr)
            
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
        
        return result

'''
Approach: Official LC iterative solution.
- Iterate a loop of size n
- Multiply the curr with 10 if it is within the limit
- Else, keep dividing curr by 10 if it ends with 9 (as next after 119 should be 12, not 120)
or out of the limit.
- Increment curr with 1 to continue the cycle
'''
