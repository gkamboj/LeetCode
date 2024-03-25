class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Node(val, val))
        else:
            self.stack.append(Node(val, min(val, self.stack[-1].min_val)))

    def pop(self) -> None:
        return self.stack.pop().val

    def top(self) -> int:
        return self.stack[-1].val
        

    def getMin(self) -> int:
        return self.stack[-1].min_val
        

class Node:
    
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Approach: Make stack of custom Node objects instead of values to maintain minimum value till every value.