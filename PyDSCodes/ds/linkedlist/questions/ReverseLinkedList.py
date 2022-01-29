from ds.linkedlist.implementations.LinkedList import LinkedList


def reverseLinkedList(linkedList):
    currHead = linkedList.head
    prev = None
    while currHead:
        newHead = currHead.next
        currHead.next = prev
        prev = currHead
        currHead = newHead
    linkedList.head = prev


def helper(nodesDataList):
    linkedList = LinkedList.createLinkedList(nodesDataList)
    print("Original linked list: ", end=" ")
    linkedList.printList()
    reverseLinkedList(linkedList)
    print("Reverse linked list: ", end=" ")
    linkedList.printList()


helper([1, 2, 3, 4, 5])
