class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i, j, ind, row = 2 * (numRows - 1), 0, 0, 0
        ans = ''
        while i >= 0:
            inc = j
            while ind <= len(s) - 1:
                ans += s[ind]
                inc = self.get_increment(i, j, inc)
                ind += inc
            i -= 2
            j += 2
            row += 1
            ind = row
        return ans

    def get_increment(self, i, j, inc):
        if i * j == 0:
            return max(i, j)
        if i == inc:
            return j
        if j == inc:
            return i
                
# Approach: Take example of any rows, say 3 or 4. Observe that first row will have character at 
# difference of indexes 2 * (numRows - 1). For eg., for numRows = 4, first row indexes will be 
# 0, 6, 12, and so on. For next row, they will be 1, 5, 7, 11, 13, and so on. That is, difference
# in a row is alternating between 2 increments, say i and j; with (i, j) being:
# 1st row: (i, j) = (6, 0)
# 2nd row: (i, j) = (4, 2)
# 3rd row: (i, j) = (2, 4)
# 4th row: (i, j) = (0, 6)
# Also, first index of every row will be the row number. Output can be finalised using (i, j) pairs.