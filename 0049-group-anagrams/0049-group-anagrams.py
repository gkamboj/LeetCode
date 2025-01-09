class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for val in strs:
            result[''.join(sorted(val))].append(val)
        return list(result.values())