class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr, chunks, sortedSum, currSum = sorted(arr)[:], 0, 0, 0
        for i in range(len(arr)):
            currSum += arr[i]
            sortedSum += sortedArr[i]
            chunks += int(currSum == sortedSum)
        return chunks
    
#Approach: Create an auxiliary sorted array. Iterate over arrays and store sum of both arrays. Increase the counter when both sums become equal.
