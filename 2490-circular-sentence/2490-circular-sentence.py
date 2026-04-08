class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        words = sentence.strip().split(' ')
        for ind, word in enumerate(words[1:], start = 1):
            if word[0] != words[ind - 1][-1]:
                return False

        return True
