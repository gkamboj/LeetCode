class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = version1.split('.'), version2.split('.')
        for ind in range(max(len(l1), len(l2))):
            val1 = l1[ind] if ind < len(l1) else '0'
            val2 = l2[ind] if ind < len(l2) else '0'
            if int(val1) > int(val2):
                return 1
            elif int(val1) < int(val2):
                return -1
        return 0
    
'''
Approach: Split both strings from '.' and compare the integer part of every member of splitted list.
'''
