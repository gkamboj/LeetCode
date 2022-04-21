# We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y. For
# example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively. The first and the
# third bit differ, so f(2, 7) = 2. You are given an array of N positive integers, A1, A2,..., AN. Find sum of f(Ai,
# Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.

def diffBitsSumPairwise(arr):
    ans = 0
    for i in range(32):
        ones = 0
        for num in arr:
            ones += (num >> i) & 1
        ans += abs(len(arr) - ones) * ones * 2
    return ans % (10 ** 9 + 7)


print(diffBitsSumPairwise([1, 3, 5]))

# Approach: Since there can be maximum 32 bits in integer, for every bit position check the number of sit and unset
# bits. From these values, we can get the contribution of ith bit to the answer from (set_bits * unset_bits * 2) [
# multiplying by 2 because every pair will occur twice: (a, b) and (b, a)]. Taking the sum of this contribution of
# every bit will give the answer.
