class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        rightMinArr = [0 for i in range(len(arr))]
        rightMinArr[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            rightMinArr[i] = min(arr[i], rightMinArr[i + 1])
        leftMax, chunks = arr[0], 1
        for i in range(len(arr) - 1):
            leftMax = max(leftMax, arr[i])
            if leftMax <= rightMinArr[i + 1]:
                chunks += 1
        return chunks
    
#Approach: Create an auxiliary array to store minimum value from end at every index. Travers array from start and keep updating maximum value till now. If this max value is less than the right min, then increment the chunks. Note that chunks has been initialsed to 1 (and not 0) as there will be atleast one chunk of whole array even if our condition is never satisfied. O(N) space & O(N) time.