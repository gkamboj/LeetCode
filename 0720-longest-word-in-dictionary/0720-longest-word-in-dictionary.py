class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ''
        words_set, pre = set(words), set()

        words.sort()
        
        for word in words:
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                if word in pre:
                    ans = word
                    continue
                curr = ''
                for char in word:
                    curr += char
                    if curr in words_set:
                        pre.add(curr)
                    else:
                        break
                else:
                    ans = word
        
        return ans
