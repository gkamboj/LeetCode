class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        freq = defaultdict(int)
        for ind in range(len(s1)):
            self.decreaseDictFreq(s1, freq, ind)
            self.increaseDictFreq(s2, freq, ind)
        
        for ind in range(len(s1), len(s2)):
            if len(freq) == 0:
                return True
            self.increaseDictFreq(s2, freq, ind)
            self.decreaseDictFreq(s2, freq, ind - len(s1))

        return len(freq) == 0

    def increaseDictFreq(self, s, freqDict, ind):
        freqDict[s[ind]] += 1
        if freqDict[s[ind]] == 0:
            del freqDict[s[ind]]

    def decreaseDictFreq(self, s, freqDict, ind):
        freqDict[s[ind]] -= 1
        if freqDict[s[ind]] == 0:
            del freqDict[s[ind]]