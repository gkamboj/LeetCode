# Given three integers A, B, and C, where A represents n, B represents r, and C represents p and p is a prime number
# greater than equal to n, find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p. Consider 1
# as prime.

def nCr_mod_p(n, r, p):
    if r > n // 2:
        r = n - r
    numerator, denominator = 1, 1
    while r > 0:
        numerator *= n
        denominator *= r
        r -= 1
        n -= 1
        if numerator >= p:
            numerator %= p
        if denominator >= p:
            denominator %= p
    return (numerator * power(denominator, p - 2, p)) % p


def power(n, pow, p):
    result = 1
    while pow > 0:
        if pow % 2 == 1:
            result = (result * n) % p
            pow -= 1
        pow //= 2
        n = (n * n) % p
    return result


print(nCr_mod_p(6, 2, 13))
print(nCr_mod_p(8492, 5152, 552011))

# Approach: By Fermat's Theorem:
#    A^(p - 1) % p = 1 where p is prime s.t. GCD(A, p) = 1
# => A^(p - 1) % p = 1 % p
# => A^(p - 2) % p = (1 / A) % p ----> inverse modulo
# Now, we have to find (num/denom) % p where num = n.(n - 1).(n - 2)....(n-r+1) and denom = r.(r-1).(r-2)....1
# From inverse modulo result: (num/denom) % p = (num * denom^(p - 2) % p) % p
# Also, to further solve the power in denom part:
# n^pow % p = (n^2)^(pow//2) % p = (n^4)^(pow//4) % p.... => refer power(n, pow, p) method
