class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        if k == n:
            return True

        for ind, row in enumerate(mat):
            for row_ind, val in enumerate(row):
                if ind % 2 and val != row[row_ind - k]:
                    return False
                elif (not ind  % 2) and val != row[(row_ind + k) % n]:
                    return False
        
        return True
            