# Y ou are given 2 numbers P and Q. An operation on these 2 numbers is defined as follows: Take the smaller number of
# the 2 numbers and subtract it from the bigger number. Keep performing this operation till either of the following
# criterion is met:
# 1. Both numbers become equal.
# 2. Either of the number becomes 0.
# Find the sum of the final values of P and Q.

def repeatedSubtraction(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return 2 * a


print(repeatedSubtraction(5, 15))
print(repeatedSubtraction(0, 2))

# Approach: Observe that repeated subtraction just means the GCD of given numbers, but the answer to problem will not
# be the GCD. It'll be twice the GCD because we need to return the sum of both numbers when they become equal (which
# is twice of GCD). Remember to handle the case when either of the given numbers is 0 at starting itself,
# then we need to return non-zero number and not the 2 * GCD.
