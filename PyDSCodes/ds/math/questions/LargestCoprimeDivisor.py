# You are given two positive numbers A and B . You need to find the maximum valued integer X such that:
# 1. X divides A i.e. A % X = 0
# 2. X and B are co-prime i.e. gcd(X, B) = 1

def largestCoprimeDivisor(a, b):
    while gcd(a, b) != 1:
        a //= gcd(a, b)
    return a


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


print(largestCoprimeDivisor(5, 10))

# Approach: Largest number dividing A which is also coprime to B will be when we have removed all the common factors
# between A & B. To remove common factors, keep dividing A with GCD(A, B) till GCD > 1.
