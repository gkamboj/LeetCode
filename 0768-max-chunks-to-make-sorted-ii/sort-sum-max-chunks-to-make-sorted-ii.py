class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr, chunks, sortedSum, currSum = sorted(arr)[:], 0, 0, 0
        for i in range(len(arr)):
            currSum += arr[i]
            sortedSum += sortedArr[i]
            chunks += int(currSum == sortedSum)
        return chunks
    
#Approach: Create an auxiliary sorted array. Iterate over arrays and store sum of both arrays. Increase the counter when both sums become equal.
#This works because once array is sorted, sum till a given index i can only be same if original array also contains same elements as sorted array.
#If original array was to contain different elements (which means greater elements than the sorted part), then sum would never have been same.
