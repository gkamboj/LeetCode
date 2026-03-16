class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        for ind in range(math.ceil(min(len(matrix), len(matrix[0])) / 2)):
            res += self.outerSpiral(matrix, ind)
        return res

    def outerSpiral(self, matrix, start):
        r_end, c_end = len(matrix) - start, len(matrix[0]) - start
        if c_end - start == 1:
            return [row[start] for row in matrix[start : r_end]]
        
        res = matrix[start][start : c_end]
        
        ind = start + 1
        while ind < r_end - 1:
            res.append(matrix[ind][-start-1])
            ind += 1
        
        if r_end - 1 != start:
            res.extend(matrix[-start-1][start : c_end][::-1])
        
        ind = r_end - 2
        while ind > start:
            res.append(matrix[ind][start])
            ind -= 1
        
        return res
