class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result, loopEnd = [], ((min(len(matrix), len(matrix[0])) - 1) // 2) + 1
        print("loopEnd: ", loopEnd)
        for i in range(loopEnd):
            result += self.outerSpiral(matrix, i)
        return result


    def outerSpiral(self, matrix, start):
        spiral, colEnd, rowEnd = [], len(matrix[0]) - start, len(matrix) - start
        if colEnd - start == 1:
            return [row[start] for row in matrix[start:rowEnd]]
        
        spiral.extend(matrix[start][start:colEnd])
        
        row = start + 1
        while row < rowEnd - 1:
            spiral.append(matrix[row][-start-1])
            row += 1
        
        if start != rowEnd - 1:
            spiral.extend(matrix[-start-1][start:colEnd][::-1])
        
        row = rowEnd - 2
        while row > start:
            spiral.append(matrix[row][start])
            row -= 1
        
        print("start: ", start, " spiral: ", spiral)
        return spiral
        
# Approach: Start from the outermost rectangle and cover the inner rectangles one by one. Handle edge cases like a single column 
# to avoid duplication.

# Check both iterative solutions of NC for shorter approaches.
