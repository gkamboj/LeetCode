class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.helper(s, 0, [], result)
        return result

    def helper(self, s, start, ip, result):
        if len(ip) == 4 and start == len(s):
            result.append('.'.join(ip))
            return
        elif start == len(s) or len(ip) == 4:
            return  
        
        if not ((4 - len(ip)) <= len(s) - start <= (4 - len(ip))  * 3):
            return

        for length in range(1, 4):
            if length + start > len(s):
                break
            
            part = s[start : start + length]

            if length > 1 and s[start] == '0':
                break
            if length == 3 and part > '255':
                break

            ip.append(part) # Append and pop instead of passing new list everytime using ip + [part] as paraneter to helper
            self.helper(s, start + length, ip, result)
            ip.pop()

'''
Approach: Backtracking
Backtrack with a start pointer, trying segment lengths 1–3 at each step. Prune if the remaining characters don't fit in the remaining parts.
Break (not continue) on leading zero or segment > "255" since longer lengths will also be invalid.
This is better than the other backtracking approach, as this avoids unnecessary memory allocation at every recursion node.
'''
