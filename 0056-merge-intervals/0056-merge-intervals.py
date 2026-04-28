class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans, ind, prev = [], 1, intervals[0]

        while ind < len(intervals):
            curr = intervals[ind]
            if curr[0] <= prev[1] <= curr[1] or curr[1] < prev[1]:
                prev[1] = max(curr[1], prev[1])
            else:
                ans.append(prev)
                prev = curr
            ind += 1
        
        ans.append(prev)

        return ans