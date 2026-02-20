class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        for ind, val in enumerate(intervals):
            if val[0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[ind:]
            elif val[1] < newInterval[0]:
                ans.append(val)
            else:
                newInterval = [min(newInterval[0], val[0]), max(newInterval[1], val[1])]
        ans.append(newInterval)
        
        return ans

# Approach: Traverse over the array, and:
# (1) If input's right value is lower than current interval's left value, add input to ans and return
# after adding remaining intervals. This is because input is already inserted.
# (2) If input's left is greater than current interval's right, add current interval to ans.
# (3) The remaining case is when input clashes with current interval. Update input for subsequent iterations.
# Append input to ans before returning.
