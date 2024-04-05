class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        ans, ind = '', 0
        while ind < n:
            if ind < n -1 and self.areCharsToBeReplaced(s[ind], s[ind + 1]):
                ind += 2
            elif ans and self.areCharsToBeReplaced(ans[-1], s[ind]):
                ans = ans[:-1]
                ind += 1
            else:
                ans += s[ind]
                ind += 1

        return ans
            
            
    def areCharsToBeReplaced(self, char1, char2):
        return (char1.islower() and char2.isupper() and char2 == char1.upper()) \
        or (char2.islower() and char1.isupper() and char1 == char2.upper())