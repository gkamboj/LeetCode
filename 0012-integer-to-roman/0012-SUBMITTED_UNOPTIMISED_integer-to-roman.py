class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        sub_mappings = {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
        ans = ''
        while num > 0:
            map_num = self.get_highest_after_num(mappings, num)
            sub_map_num = self.get_highest_after_num(sub_mappings, num)
            if map_num > sub_map_num:
                ans += (mappings[map_num] * (num // map_num))
                num %= map_num
            else:
                num %= sub_map_num
                ans += sub_mappings[sub_map_num]
        return ans
    
    def get_highest_after_num(self, mappings, num):
        for key in mappings:
            if key <= num:
                return key
        return 0
