class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for word in strs:
            ana_map[''.join(sorted(word))].append(word)
        return list(ana_map.values())