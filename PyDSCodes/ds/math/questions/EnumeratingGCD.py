# You are given a number A and a number B. Greatest Common Divisor (GCD) of all numbers between A and B inclusive is
# taken (GCD(A, A+1, A+2 ... B)). A and B can be in the range of 10100. Return the value of GCD found.

def enumeratingGCD(a, b):
    if a == b:
        return a
    return 1


print(enumeratingGCD(1, 3))

# Approach: Since A and B can be very large and so can be the difference between them, it's not advisable to find GCD
# for such a large range. Instead, observe that if A != B, GCD will always be equal to 1. This is because GCD(x,
# x + 1) = GCD(x, (x + 1) - x) = 1. When A == B, GCD = A.
