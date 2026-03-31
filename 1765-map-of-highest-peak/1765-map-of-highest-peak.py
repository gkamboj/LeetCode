class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        result, queue = [], deque()
        for i, row in enumerate(isWater):
            temp = []
            for j, val in enumerate(row):
                if val:
                    temp.append(0)
                    queue.append((i, j, 0))
                else:
                    temp.append(-1)
            result.append(temp)

        while queue:
            i, j, val = queue.popleft()
            self.update_matrix(result, queue, i - 1, j, val)
            self.update_matrix(result, queue, i + 1, j, val)
            self.update_matrix(result, queue, i, j - 1, val)
            self.update_matrix(result, queue, i, j + 1, val)

        return result

    
    def update_matrix(self, matrix, queue, i, j, val):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == -1:
            matrix[i][j] = val + 1
            queue.append((i, j, val + 1))