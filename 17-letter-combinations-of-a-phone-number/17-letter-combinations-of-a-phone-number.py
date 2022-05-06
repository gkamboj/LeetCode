class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d, asciiVal = {}, 97
        for i in range(2, 10):
            if i != 7 and i != 9:
                d[str(i)] = [chr(j) for j in range(asciiVal, asciiVal + 3)]
                asciiVal += 3
            else:
                d[str(i)] = [chr(j) for j in range(asciiVal, asciiVal + 4)]
                asciiVal += 4
        
        result = [""]
        while len(result[0]) != len(digits):
            curr = result.pop(0)
            currDigit = d[str(digits[len(curr)])]
            for char in currDigit:
                result.append(curr + char)
                
        return result
    
# Approach: This is iterative approach. Start by popping out first element of result and append it to every character from current digit one by one, and append these to result. Continue till all the digits are iterated.

# Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8064/My-java-solution-with-FIFO-queue