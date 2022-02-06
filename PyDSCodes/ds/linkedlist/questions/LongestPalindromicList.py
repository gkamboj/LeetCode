from ds.linkedlist.implementations.LinkedList import LinkedList


def findLongestPalindrome(linkedList):
    curr = linkedList.head
    prev, result = None, 1
    while curr:
        newHead = curr.next
        curr.next = prev
        result = max(result, findPalindromeLength(curr, newHead))
        result = max(result, findPalindromeLength(prev, newHead) + 1)
        prev = curr
        curr = newHead
    return result


def findPalindromeLength(left, right):
    length = 0
    while left and right:
        if left.data == right.data:
            length += 2
        else:
            break
        left = left.next
        right = right.next
    return length


def helper(list):
    linkedList = LinkedList.createLinkedList(list)
    print("Given linked list: ", end=" ")
    linkedList.printList()
    print(findLongestPalindrome(linkedList))
    print()


helper([2, 1, 2, 1, 2, 2, 1, 3, 2, 2])
helper([1])
helper([1, 2])
helper([1, 1])
helper([2, 3, 3, 3])
helper([1, 2, 1, 2, 1, 2, 3, 2, 1])

# Approach: Firstly, remember that there can be two types of palindrome: even length and odd length. Odd
# length will have a middle element whereas even length will have 2 middle elements. 1. Brute force approach is O(
# N^3): double for loop to get every possible pair of start and end, and then another N factor for checking
# palindrome
#
# 2. An improvement over brute force that can be done is creating another linked list which is reverse of
# given list. Then for every node check the longest palindrome having that node as mid. This will reduce the O(N^2)
# factor to O(N) and hence total complexity will be O(N^2). Remember to take care of both odd and even length cases.
#
# 3. We can further optimise the above solution by reducing the O(N) space to O(1): We can do the both reversal and
# finding max length simultaneously. While reversing the list, find the max length palindrome at every step for both
# odd and even length cases. For odd length cases, we will use prev and next of curr, while for even length cases we
# will use curr and next.
