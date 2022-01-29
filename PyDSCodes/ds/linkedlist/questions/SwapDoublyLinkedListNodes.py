from ds.linkedlist.implementations.DoublyLinkedList import DoublyLinkedList


def swapNodes(doublyLinkedList, node1Data, node2Data):
    if doublyLinkedList.head.data == node2Data:
        swapNodes(doublyLinkedList, node2Data, node1Data)
        return
    node1 = doublyLinkedList.getNode(node1Data)
    node2 = doublyLinkedList.getNode(node2Data)

    if node1.next and node1.next.data == node2.data:
        swapAdjacentNodes(doublyLinkedList, node1, node2)
    elif node2.next and node2.next.data == node1.data:
        swapNodes(doublyLinkedList, node2Data, node1Data)
        return
    elif not node1.prev:
        swapHeadAndNode(doublyLinkedList, node1, node2)
    else:
        swapNonAdjacentNodes(doublyLinkedList, node1, node2)


def swapHeadAndNode(doublyLinkedList, head, node):
    currHeadNext = head.next
    node.prev.next = head
    head.prev = node.prev
    if node.next:
        node.next.prev = head
        head.next = node.next
    else:
        doublyLinkedList.tail = head
        head.next = None
    node.next = currHeadNext
    currHeadNext.prev = node
    doublyLinkedList.head = node
    node.prev = None


def swapAdjacentNodes(doublyLinkedList, node1, node2):
    if node1.prev:
        node1.prev.next = node2
        node2.prev = node1.prev
    else:
        doublyLinkedList.head = node2
        node2.prev = None
    node1.next = node2.next
    if node2.next:
        node2.next.prev = node1
    else:
        doublyLinkedList.tail = node1
    node2.next = node1
    node1.prev = node2


def swapNonAdjacentNodes(doublyLinkedList, node1, node2):
    if not node1.next:  # I want that if there one of the nodes is tail, then it should be node2
        swapNonAdjacentNodes(doublyLinkedList, node2, node1)
        return
    currNode1Prev = node1.prev
    currNode1Next = node1.next
    node2.prev.next = node1
    node1.prev = node2.prev
    if node2.next:
        node2.next.prev = node1
        node1.next = node2.next
    else:
        node1.next = None
        doublyLinkedList.tail = node1
    node2.prev = currNode1Prev
    currNode1Prev.next = node2
    node2.next = currNode1Next
    currNode1Next.prev = node2


def swapAndPrint(list, node1, node2):
    doublyLinkedList = DoublyLinkedList.createLinkedList(list)
    print("Original linked list: ")
    doublyLinkedList.printList()
    doublyLinkedList.printListFromEnd()
    print("Swapping " + str(node1) + " and " + str(node2))
    swapNodes(doublyLinkedList, node1, node2)
    print("Resultant list after swapping: ")
    doublyLinkedList.printList()
    doublyLinkedList.printListFromEnd()
    print()


# Head case
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 8, 1)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 1, 6)

# Non-adjacent
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 6)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 8)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 7)

# Adjacent cases
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 4)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 1, 2)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 6, 7)

# Only 2 nodes in list
swapAndPrint([2, 3], 2, 3)
