class Solution:
     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, pos, currPos, currSum = [], [], 0, 0
        candidates.sort()
        
        while currPos < len(candidates):
            if currSum == target:
                result.append([candidates[i] for i in pos])
                currSum -= candidates[pos.pop()]
                currPos += 1
            elif currSum < target:
                pos.append(currPos)
                currSum += candidates[currPos]
            else:
                temp = 2
                while pos and temp > 0:
                    temp -= 1
                    currPos = pos.pop()
                    currSum -= candidates[currPos]
                currPos += 1
            
            while currPos >= len(candidates) and pos:
                currPos = pos.pop() + 1
                currSum -= candidates[currPos - 1]
            
        return result