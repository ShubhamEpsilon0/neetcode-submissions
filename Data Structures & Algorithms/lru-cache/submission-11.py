class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertRear(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node):
        if node == self.head or node == self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeFront(self):
        node = self.head.next
        self.removeNode(node)
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.LRUOrderList = DoublyLinkedList()
        self.KeyMap = {}
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.KeyMap:
            return -1

        self.LRUOrderList.removeNode(self.KeyMap[key])
        self.LRUOrderList.insertRear(self.KeyMap[key])

        return self.KeyMap[key].val[1]


    def put(self, key: int, value: int) -> None:
        node = None
        if key not in self.KeyMap:
            node = Node((key, value))
            self.KeyMap[key] = node
            if len(self.KeyMap) > self.capacity:
                node1 = self.LRUOrderList.removeFront()
                if node1:
                    del self.KeyMap[node1.val[0]]
        else:
            node = self.KeyMap[key]
            self.LRUOrderList.removeNode(node)
            node.val = (key, value)
        self.LRUOrderList.insertRear(node)

        

        
