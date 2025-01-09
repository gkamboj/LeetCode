class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for val in strs:
            curr = [0]*26
            for char in val:
                curr[ord(char) - ord('a')] += 1
            result[tuple(curr)].append(val)

        return list(result.values())

# Approach: Similar to approach with sorting, but using array to detect anagram words instead of sorting each word
