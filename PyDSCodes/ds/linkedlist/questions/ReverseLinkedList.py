from ds.linkedlist.implementations.LinkedList import LinkedList


def reverseLinkedListIteratively(linkedList):
    currHead = linkedList.head
    prev = None
    while currHead:
        newHead = currHead.next
        currHead.next = prev
        prev = currHead
        currHead = newHead
    linkedList.head = prev


def reverseLinkedListRecursively(head):
    if not head or not head.next:
        return head
    rest = reverseLinkedListRecursively(head.next)
    head.next.next = head
    head.next = None
    return rest


def reverseLinkedListRecursively2(head, prev):
    if not head:
        return prev
    newHead = head.next
    head.next = prev
    return reverseLinkedListRecursively2(newHead, head)


def helper(nodesDataList):
    linkedList = LinkedList.createLinkedList(nodesDataList)
    print("Original linked list: ", end=" ")
    linkedList.printList()
    reverseLinkedListIteratively(linkedList)
    print("Reversed linked list through iteration: ", end=" ")
    linkedList.printList()
    linkedList.head = reverseLinkedListRecursively(linkedList.head)
    print("Reversed linked list through recursion: ", end=" ")
    linkedList.printList()
    linkedList.head = reverseLinkedListRecursively2(linkedList.head, None)
    print("Reversed linked list through recursion (way 2): ", end=" ")
    linkedList.printList()
    print()

helper([1, 2, 3, 4, 5])
helper([1])
