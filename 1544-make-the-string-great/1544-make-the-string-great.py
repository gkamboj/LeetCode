class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        ans, ind = '', 0
        while ind < n:
            if ind < n -1 and abs(ord(s[ind+1]) - ord(s[ind])) == 32:
                ind += 2
            elif ans and abs(ord(ans[-1]) - ord(s[ind])) == 32:
                ans = ans[:-1]
                ind += 1
            else:
                ans += s[ind]
                ind += 1

        return ans
            
            
    