# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing
# the order of the remaining elements. For example, the sequence {2, 3, 5} is a subsequence of {1, 2, 3, 4,
# 5} obtained after removal of elements {1, 4}. Given is an array of integers A of size N. An array of size N can
# have (2^N - 1) number of non empty subsequences. For the given function:
# #  solve (int subsequence[]) {
# #     int count[];    //array initialised to 0.
# #     for(int i = 0; i &amp;lt; subsequence.length; i++) {
# #         number = subsequence[i];
# #         for(int j = 2; j &amp;lt;= number; j++) {
# #             if(number % j == 0) {
# #                 count[j]++;
# #                 if(count[j] == subsequence.length)  return 0;
# #             }
# #         }
# #     }
# #     return 1;
# # }
# If all the subsequences of the array A are passed in the above function. What will be the bitwise OR of all the
# returned values from the given function.

def solveSubseqAndReturnOR(arr):
    if len(arr) == 1 or arrayGCD(arr) == 1:
        return 1
    return 0


def arrayGCD(arr):
    gcdVal = gcd(arr[0], arr[1])
    for num in arr[2:]:
        gcdVal = gcd(gcdVal, num)
    return gcdVal


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


print(solveSubseqAndReturnOR([2, 4, 6]))
print(solveSubseqAndReturnOR([1, 2, 3]))

# Approach: Observe that given method is returning 1 if GCD of passed sequence is 1, else it's returning 0. Now,
# if GCD of any sequence is 1, then the GCD of whole array will also be 1. So, just find the GCD of array and return
# 1 if GCD is 1, else 0. Remember to handle the case when array length is 1 separately.
