class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        result = []
        for query in queries:
            if query[0] == 0:
                result.append(arr[query[1]])
            else:
                result.append(arr[query[1]] ^ arr[query[0] - 1])
        return result