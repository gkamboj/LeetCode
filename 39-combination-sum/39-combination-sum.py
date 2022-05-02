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
    
# Approach: This is iterative approach. Following is the dry run for input [3, 7, 2, 6]:
#   currSum           tempList            posList             pos
#       2               [2]                 [0]                 0
#       4              [2, 2]              [0, 0]               0
#       6             [2, 2, 2]           [0, 0, 0]             0
#       8            [2, 2, 2, 2]        [0, 0, 0, 0]           0
#       4               [2, 2]             [0, 0]               1
#       7             [2, 2, 3]           [0, 0, 1]             1
#       4               [2, 2]              [0, 0]              2
#       11            [2, 2, 6]            [0, 0, 2]            2
#       2                [2]                 [0]                3
#       0                 []                  []                1

# Reference: https://leetcode.com/problems/combination-sum/discuss/391125/Explanation-for-backtracking-solution-using-iteration-python-implementation-beats-90