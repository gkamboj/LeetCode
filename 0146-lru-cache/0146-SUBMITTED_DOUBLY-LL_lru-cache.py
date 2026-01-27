class LRUCache:

    def __init__(self, capacity: int):
        self.capacity, self.cache = capacity, {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
        
        self.addNode(node)
        
        if len(self.cache) > self.capacity:
            # print("key ", key, "value ", value, "head ", self.head)
            lruNode = self.head.next
            self.removeNode(lruNode)
            del self.cache[lruNode.key]


    def removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def addNode(self, node):
        prev = self.tail.prev
        prev.next = self.tail.prev = node
        node.next, node.prev = self.tail, prev


class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

# Approach: Using a custom doubly linked list. Move the node with the passed key to the end for every get call. Similar for put too
# for existing key and insertion at the end for new keys.

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
