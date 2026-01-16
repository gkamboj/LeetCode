class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for val in strs:
            encoded_str += str(len(val)) + '#' + val
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result, ind = [], 0
        while ind < len(s):
            count = ''
            while s[ind] != '#':
                count += s[ind]
                ind += 1
            ind += 1
            curr, curr_end = '', ind + int(count)
            while ind < curr_end:
                curr += s[ind]
                ind += 1
            result.append(curr)
        return result
                
