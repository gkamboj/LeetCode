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