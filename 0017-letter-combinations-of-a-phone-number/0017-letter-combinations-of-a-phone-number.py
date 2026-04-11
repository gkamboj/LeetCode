class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs_size = {'7': ('p', 4), '8': ('t', 3), '9': ('w', 4)}
            
        ans = ['']
        for digit in digits:
            start_char, char_count = combs_size.get(digit, ('', 3))
            if not start_char:
                start_char = chr(ord('a') + (int(digit) - 2) * 3)
            chars = []
            temp = []
            for val in ans:
                temp += [val + letter for letter in [chr(ord(start_char) + val) for val in range(char_count)]]
            ans = temp
        
        return ans

'''
Approach: 
'''