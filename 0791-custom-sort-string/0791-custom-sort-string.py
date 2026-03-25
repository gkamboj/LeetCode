class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pos, pos_dict = 1, defaultdict(int)
        for char in order:
            pos_dict[char] = pos
            pos += 1
        
        chars = ['' for i in range(pos + 1)]
        for char in s:
            chars[pos_dict[char]] += char
        
        return ''.join(chars)

'''
Approach: Store the order in a dictionary. Then for every char, store characters of s
in array according the input order. Join the array to get final answer
'''