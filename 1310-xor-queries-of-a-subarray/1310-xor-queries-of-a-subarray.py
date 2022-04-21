class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorPrefix, result = [0], []
        for num in arr:
            xorPrefix.append(xorPrefix[-1] ^ num)
        for query in queries:
            result.append(xorPrefix[query[1] + 1] ^ xorPrefix[query[0]])
        return result
        