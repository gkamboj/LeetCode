class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        if k == len(mat[0]):
            return True

        for ind, row in enumerate(mat):
            if ind % 2:
                temp = row[-k:] + row[:-k]
            else:
                temp = row[k:] + row[:k]
            if temp != row:
                return False
        
        return True
            