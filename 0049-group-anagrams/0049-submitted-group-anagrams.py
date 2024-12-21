class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            result[''.join(sorted(word))].append(word)
        return list(result.values())
    
# Approach: Create a dictionary with key as sorted string of every element, so value for every key will be a list of anagram strings. 
# Note: dict.values() returns view of list, not the list itself since recent Python versions. So, wrap it in list() before returning.
