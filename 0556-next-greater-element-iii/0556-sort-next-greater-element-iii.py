class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_str, temp, invalid = str(n), [], True
        for ind in range(len(n_str) - 1, -1, -1):
            if temp and n_str[ind] < temp[-1]:
                temp.append(n_str[ind])
                invalid = False
                break
            else: temp.append(n_str[ind])
        if invalid: return -1
        temp.sort()
        for num in temp:
            if num > n_str[ind]:
                temp.remove(num)
                next_greater = num
                break
        ans = int(n_str[:ind] + next_greater + ''.join(temp))
        return ans if ans < 2**31 else -1
    
''' Approach: Start from the end and traverse till we reach digit (at say index ind with value val) greater 
than next digit. Sort the digits from [ind : len(n)], remove the digit (say x) just greater than val and 
return (digits till ind - 1) + x + sorted part.
'''
