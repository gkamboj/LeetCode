class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        minFromEnd, chunks = arr[:], 1
        for i in range(len(arr) - 2, -1, -1):
            if minFromEnd[i + 1] < arr[i]:
                minFromEnd[i] = minFromEnd[i + 1]
        currMax = arr[0]
        for i in range(len(arr) - 1):
            currMax = max(arr[i], currMax)
            if currMax <= minFromEnd[i + 1]:
                chunks += 1
        return chunks