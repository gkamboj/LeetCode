# Given an integer A, find and return the Ath magic number. A magic number is defined as a number that can be
# expressed as a power of 5 or a sum of unique powers of 5. First few magic numbers are 5, 25, 30(5 + 25), 125,
# 130(125 + 5),

def nthMagicNumber(n):
    ans, power = 0, 0
    while n > 0:
        power += 1
        ans += (5 ** power) * (n % 2)
        n //= 2
    return ans


print(nthMagicNumber(10))

# Approach: Expressing a number as power of 5 is similar to binary number representation (where we express a number
# as sums of power of 2). So, find binary representation of the given number and create new decimal number from it
# with base as 5 instead of 2.
