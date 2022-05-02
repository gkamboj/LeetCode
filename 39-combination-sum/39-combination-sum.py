class Solution:
     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        
        candidates.sort()        
        if n<=0 or candidates[0] <= 0:
            return []
        
        subSets, tempList, posList = [], [], []
        currSum = pos = 0
        
        while pos < n:
            if currSum > target:
                # pop curr and it's parent, because we are sorted and distinct
                # adding any more items will only increase the sum
                t = 2
                while tempList and t:
                    currSum -= tempList.pop()
                    pos = posList.pop()
                    t -= 1
                pos += 1
            elif currSum == target:
                # Found a subset
                subSets.append(tempList[:])
                currSum -= tempList.pop()
                pos = posList.pop()
                pos += 1
            else:
                currSum += candidates[pos]
                tempList.append(candidates[pos])
                posList.append(pos)
            
            # At the end of each level, check if we still have some levels left to check
            while pos >= n and posList:
                # print("inside",tempList ,posList, currSum)
                currSum -= tempList.pop()
                pos = posList.pop() + 1
                
            # print(pos, tempList ,posList, currSum)
            
        return subSets