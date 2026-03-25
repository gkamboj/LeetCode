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
Approach: Store the order in a dictionary. Then, for every character of s, add it to
the array according to the input order. Join the array to get the final answer
'''
