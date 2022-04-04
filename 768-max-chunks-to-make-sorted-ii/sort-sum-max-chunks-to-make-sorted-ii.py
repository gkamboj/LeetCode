class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr = arr[:]
        sortedArr.sort()
        arrSum, sortedArrSum, chunks = 0, 0, 0
        for i in range(len(arr)):
            arrSum += arr[i]
            sortedArrSum += sortedArr[i]
            if arrSum == sortedArrSum:
                chunks += 1
        return chunks
    
#Approach: Create an auxiliary sorted array. Iterate over arrays and store sum of both arrays. Increase the counter when both sums become equal.