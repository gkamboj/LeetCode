class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people) - 1
        ans = 0
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            ans += 1
        return ans
    
'''
Approach: Use 2 pointers, increase start pointer if people[start] + people[end] <= limit because this allows
wight of person at start index also to be included to the current boat.
'''
