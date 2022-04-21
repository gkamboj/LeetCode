# You have an array A with N elements. We have two types of operation available on this array :
# 1. We can split an element B into two elements, C and D, such that B = C + D.
# 2. We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
# You have to determine whether it is possible to convert array A to size 1, containing a single element
# equal to 0 after several splits and/or merge?

def interestingArray(arr):
    oddCount = 0
    for num in arr:
        oddCount += (num % 2)
    return "No" if oddCount % 2 else "Yes"

# Approach: Since x^x = 0, every even number can be split into its half and then merged to make it 0. For odd
# numbers, every two odd numbers can be combined to make it even and then make it zero. So, answer will depend on the
# count of odd numbers: if there are even number of odd elements in array then "Yes", else "No"
