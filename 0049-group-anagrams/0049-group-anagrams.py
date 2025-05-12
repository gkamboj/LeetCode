class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for word in strs:
            counter = self.counter(word)
            ana_map[counter].append(word)
        return list(ana_map.values())

    def counter(self, word):
        counter = [0 for i in range(26)]
        for char in word:
            counter[ord(char) - ord('a')] += 1
        return tuple(counter)