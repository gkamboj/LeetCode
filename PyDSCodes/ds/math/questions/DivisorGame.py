# Scooby has 3 three integers num, a and b.
# Scooby calls a positive integer special if it is divisible by a as well as b. You need to tell the
# number of special integers less than or equal to num.

def divisorGame(num, a, b):
    lcm = (a * b) // gcd(a, b)
    return num // lcm


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


print(divisorGame(12, 3, 2))
print(divisorGame(87120, 3859, 671))

# Approach: For a number to be divisible by both a and b, it should be divisible by LCM(a, b). Also, LCM = (a * b) /
# GCD(a, b). Once we have LCM, required count can be found out by num/lcm.
