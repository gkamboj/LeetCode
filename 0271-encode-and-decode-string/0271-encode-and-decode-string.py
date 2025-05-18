from typing import List


class Solution:

    def __init__(self):
        pass

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            result.append(s[i + 1 : i + 1 + int(size)])
            i += 1 + int(size)
        return result


words = ["neet", "code", "loves", "you", "substantially", "happily"]

obj = Solution()
# encoded_str = obj.encode(words)
# decoded_list = obj.decode(encoded_str)
# print(decoded_list == words)

# Approach: We are adding length of word as well as "#" while encoding to
# handle cases when length of word is in double digits.

def isValid(s: str) -> bool:
    chars = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []
    for b in s:
        if b in chars:
            stack.append(b)
        elif not stack or chars[stack.pop()] != b:
            return False
    return not stack

isValid("()[]{}")