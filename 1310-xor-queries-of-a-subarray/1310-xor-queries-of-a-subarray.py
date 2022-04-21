class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorPrefix, result = [0], []
        for num in arr:
            xorPrefix.append(xorPrefix[-1] ^ num)
        for query in queries:
            result.append(xorPrefix[query[1] + 1] ^ xorPrefix[query[0]])
        return result
        
#Approach: Cretate an auxiliary prefix XOR array s.t. ith element is XOR of elements upto i index. Now, for every query, XOR elements present at both query indices in auxiliary array. This works because all elements upto query[0] will be canceled out when doing XOR and only required XOR will be left.