class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None
            self.prev = None

    def swapNodes(self, node1Data, node2Data):
        if self.head.data == node1Data:
            node1 = self.head
            node1Previous = None
            node2Previous = self.getPreviousNode(node2Data)
            node2 = node2Previous.next
        elif self.head.data == node2Data:
            node2 = self.head
            node2Previous = None
            node1Previous = self.getPreviousNode(node1Data)
            node1 = node1Previous.next
        else:
            node1Previous = self.getPreviousNode(node1Data)
            node2Previous = self.getPreviousNode(node2Data)
            node1 = node1Previous.next
            node2 = node2Previous.next

        if node1.next and node1.next.data == node2.data:
            self.swapAdjacentNodes(node1Previous, node1, node2)
        elif node2.next and node2.next.data == node1.data:
            self.swapAdjacentNodes(node2Previous, node2, node1)
        elif not node1Previous:
            self.swapHeadAndNode(node1, node2, node2Previous)
        elif not node2Previous:
            self.swapHeadAndNode(node2, node1, node1Previous)
        else:
            self.swapNonAdjacentNodes(node1, node2, node1Previous, node2Previous)

    def swapHeadAndNode(self, head, node, prev):
        currHeadNext = head.next
        prev.next = head
        head.next = node.next
        node.next = currHeadNext
        self.head = node

    def swapAdjacentNodes(self, prev, node1, node2):
        if prev is not None:
            prev.next = node2
        else:
            self.head = node2
        node1.next = node2.next
        node2.next = node1

    def swapNonAdjacentNodes(self, node1, node2, node1Previous, node2Previous):
        currNode2Next = node2.next
        node1Previous.next = node2
        node2.next = node1.next
        node2Previous.next = node1
        node1.next = currNode2Next

    def getPreviousNode(self, data):
        if self.head.data == data:
            return None
        curr = self.head
        while curr.next.data != data:
            curr = curr.next
        return curr

    def push(self, new_data):
        new_Node = self.Node(new_data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            tail = self.tail
            tail.next = new_Node
            new_Node.prev = tail
            self.tail = new_Node

    def printList(self):
        curr = self.head
        while curr.next:
            print(curr.data, end=' <-> ')
            curr = curr.next
        print(curr.data)

    def printListFromEnd(self):
        curr = self.tail
        while curr.prev:
            print(curr.data, end = ' <-> ')
            curr = curr.prev
        print(curr.data)


def pushToList(nodesData):
    doublyLinkedList = DoublyLinkedList()
    for nodeData in nodesData:
        doublyLinkedList.push(nodeData)
    return doublyLinkedList


def swapAndPrint(list, node1, node2):
    linkedList = pushToList(list)
    print("Original doubly linked list: ", end=" ")
    linkedList.printList()
    print("Swapping " + str(node1) + " and " + str(node2))
    linkedList.swapNodes(node1, node2)
    print("Resultant list after swapping: ", end=" ")
    linkedList.printList()
    print()


# Head case
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 8, 1)

#Non-adjacent
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 6)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 8)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 3, 7)

# Adjacent cases
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 4, 3)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 2, 1)
swapAndPrint([1, 2, 3, 4, 8, 7, 6], 6, 7)

#Only 2 nodes in list
swapAndPrint([2, 3], 2, 3)
