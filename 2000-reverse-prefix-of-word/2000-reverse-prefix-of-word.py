class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word += '.'
        for ind, val in enumerate(word):
            if val == ch:
                word = word[:ind+1][::-1] + word[ind+1:]
                break
        return word[:-1]
    
'''
Approach: Self-explanatory code, refer official solutions for more approaches.
'''