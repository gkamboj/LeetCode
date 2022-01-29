from ds.linkedlist.implementations.LinkedList import LinkedList


def swapNodes(linkedList, node1Data, node2Data):
    if linkedList.head.data == node2Data:
        swapNodes(linkedList, node2Data, node1Data)
        return
    if linkedList.head.data == node1Data:
        node1 = linkedList.head
        node1Previous = None
        node2Previous = linkedList.getPreviousNode(node2Data)
        node2 = node2Previous.next
    else:
        node1Previous = linkedList.getPreviousNode(node1Data)
        node2Previous = linkedList.getPreviousNode(node2Data)
        node1 = node1Previous.next
        node2 = node2Previous.next

    if node1.next and node1.next.data == node2.data:
        swapAdjacentNodes(linkedList, node1Previous, node1, node2)
    elif node2.next and node2.next.data == node1.data:
        swapNodes(linkedList, node2Data, node1Data)
        return
    elif not node1Previous:
        swapHeadAndNode(linkedList, node1, node2, node2Previous)
    elif not node2Previous:
        swapNodes(linkedList, node2Data, node1Data)
    else:
        swapNonAdjacentNodes(node1, node2, node1Previous, node2Previous)


def swapHeadAndNode(linkedList, head, node, prev):
    currHeadNext = head.next
    prev.next = head
    head.next = node.next
    node.next = currHeadNext
    linkedList.head = node


def swapAdjacentNodes(linkedList, prev, node1, node2):
    if prev is not None:
        prev.next = node2
    else:
        linkedList.head = node2
    node1.next = node2.next
    node2.next = node1


def swapNonAdjacentNodes(node1, node2, node1Previous, node2Previous):
    currNode2Next = node2.next
    node1Previous.next = node2
    node2.next = node1.next
    node2Previous.next = node1
    node1.next = currNode2Next


def swapAndPrint(list, node1, node2):
    linkedList = LinkedList.createLinkedList(list)
    print("Original linked list: ", end=" ")
    linkedList.printList()
    print("Swapping " + str(node1) + " and " + str(node2))
    swapNodes(linkedList, node1, node2)
    print("Resultant list after swapping: ", end=" ")
    linkedList.printList()
    print()


# Head case
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 8, 1)

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
