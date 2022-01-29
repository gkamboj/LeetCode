class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None
            self.prev = None

    def add(self, new_data):
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
            print(curr.data, end=' <-> ')
            curr = curr.prev
        print(curr.data)

    def getNode(self, data):
        if self.head.data == data:
            return self.head
        curr = self.head
        while curr.data != data:
            curr = curr.next
        return curr

    @staticmethod
    def createLinkedList(nodesData):
        doublyLinkedList = DoublyLinkedList()
        for nodeData in nodesData:
            doublyLinkedList.add(nodeData)
        return doublyLinkedList
