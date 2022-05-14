class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr, chunks, sortedSum, currSum = sorted(arr)[:], 0, 0, 0
        for i in range(len(arr)):
            currSum += arr[i]
            sortedSum += sortedArr[i]
            chunks += int(currSum == sortedSum)
        return chunks
        