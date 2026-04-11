class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs_size = {'7': ('p', 4), '8': ('t', 3), '9': ('w', 4)}
            
        ans = ['']
        for digit in digits:
            start_char, char_count = combs_size.get(digit, ('', 3))
            if not start_char:
                start_char = chr(ord('a') + (int(digit) - 2) * 3)
            temp, letters = [], [chr(ord(start_char) + i) for i in range(char_count)]
            for val in ans:
                temp += [val + letter for letter in letters]
            ans = temp
        
        return ans

'''
Approach:
- Iteratively build all combinations using a BFS-style approach: start with `['']` and for each digit, append every possible mapped letter to existing prefixes.
- Use either a direct mapping or computed character ranges to get letters for each digit.
- At each step, replace the result list with newly formed combinations until all digits are processed.
'''