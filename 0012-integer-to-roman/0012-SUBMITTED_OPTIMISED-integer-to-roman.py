class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        ans = ''
        for val, symbol in mappings:
            div, num = divmod(num, val)
            ans += symbol * div
        return ans

'''
Approach: Iterate over Roman numeral values in descending order (including subtractive 
cases like 900, 400, etc.). At each step, get quotient and remained to determine how 
many times the value fits into num and append the corresponding symbols. Reduce num by 
the remainder and continue until it becomes zero. Since a symbol can only repeat once,
for loop on mappings will work.
'''
