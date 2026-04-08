class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for ind, char in enumerate(sentence.strip()):
            if char == ' ' and sentence[ind - 1] != sentence[ind + 1]:
                return False
        return sentence[0] == sentence[-1]

'''
Approach: Traverse over the whole sentence. When encountering a space, match the previous and next characters.
If we reach the end, compare the first and last characters of the whole sentence to get the final answer.
'''
