class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.helper(s, [], result)
        return result

    def helper(self, s, curr, result):    
        if not s:
            if len(curr) == 4:
                result.append('.'.join(curr))
            return 
        
        self.helper(s[1:], curr + [s[0]], result)

        if len(s) > 1 and int(val := s[:2]) >= 10:
            self.helper(s[2:], curr + [val], result)
        
        if len(s) > 2 and 100 <= int(val := s[:3]) <= 255:
            self.helper(s[3:], curr + [val], result)
        