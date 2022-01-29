class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    def add(self, new_data):
        new_Node = self.Node(new_data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            tail = self.tail
            tail.next = new_Node
            self.tail = new_Node

    def printList(self):
        curr = self.head
        while curr.next:
            print(curr.data, end=' -> ')
            curr = curr.next
        print(curr.data)

    def getPreviousNode(self, data):
        if self.head.data == data:
            return None
        curr = self.head
        while curr.next.data != data:
            curr = curr.next
        return curr

    @staticmethod
    def createLinkedList(nodesData):
        linkedList = LinkedList()
        for nodeData in nodesData:
            linkedList.add(nodeData)
        return linkedList
