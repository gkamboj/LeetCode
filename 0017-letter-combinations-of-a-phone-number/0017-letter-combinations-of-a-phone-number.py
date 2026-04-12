class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        self.helper(digits, 0, '', result)
        return result

    def helper(self, digits, ind, combo, result):
        if ind == len(digits):
            result.append(combo)
            return
        
        digit = digits[ind]
        if digit == '7':
            start, count = 'p', 4
        elif digit == '8':
            start, count = 't', 3
        elif digit == '9':
            start, count = 'w', 4
        else:
            start, count = chr((int(digit) - 2) * 3 + ord('a')), 3
        letters = [chr(ord(start) + i) for i in range(count)]

        for letter in letters:
            self.helper(digits, ind + 1, combo + letter, result)


'''
Approach: Backtracking
- Use backtracking to build all combinations by processing one digit at a time and appending corresponding letters.
- For each digit, compute its mapped letters, recursively explore all choices, and add the completed string when you reach the end.
'''