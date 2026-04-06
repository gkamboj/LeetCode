class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid, ans = set(['']), ''

        words.sort()

        for word in words:
            if word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word

        return ans

'''
Approach: Sort the words lexicographically and maintain a set of valid words starting with empty string.
For each word, check if its prefix `word[:-1]` exists in the set; if yes, add the word and update the answer.
This works because sorting ensures prefixes are processed before longer words.
'''
