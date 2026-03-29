class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_inds = (n + 1) // 2
        odd_inds = n - even_inds
        mod = 10**9 + 7
        return (self.power(5, even_inds, mod) * self.power(4, odd_inds, mod)) % mod

    def power(self, base, exp, mod):
        result = 1
        while exp:
            if exp % 2:
                result = (result * base) % mod
            exp //= 2
            base = (base * base) % mod
        return result