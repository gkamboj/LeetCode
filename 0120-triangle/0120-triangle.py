class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store = {}
        return self.helper(triangle, store, 0, 0)

    def helper(self, triangle, store, ind1, ind2):
        if ind1 == len(triangle) - 1:
            return triangle[ind1][ind2]
        else:

            if (key := (ind1 + 1, ind2)) in store:
                v1 = store[key]
            else:
                v1 = self.helper(triangle, store, ind1 + 1, ind2)
                store[key] = v1

            if (key := (ind1 + 1, ind2 + 1)) in store:
                v2 = store[key]
            else:
                v2 = self.helper(triangle, store, ind1 + 1, ind2 + 1)
                store[key] = v2
            
            return triangle[ind1][ind2] + min(v1, v2)