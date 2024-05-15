class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter, counter2 = defaultdict(int), defaultdict(int)
        for ind, char in enumerate(s1):
            counter[char] += 1
            counter2[s2[ind]] += 1
        for ind in range(len(s1), len(s2)):
            if self.areSameDict(counter, counter2):
                return True
            to_remove_key = s2[ind - len(s1)]
            counter2[to_remove_key] -= 1
            counter2[s2[ind]] += 1
        return self.areSameDict(counter, counter2)
    
    def areSameDict(self, dict1, dict2):
        return {k: v for k, v in dict1.items() if v > 0} == {k: v for k, v in dict2.items() if v > 0}