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
        try:
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
        except Exception as e:
            self.printForward()
            self.printBackward()
            raise

    def removeNode(self, node):
        try:
            print(node.val)
            node.prev.next = node.next
            node.next.prev = node.prev
        except Exception as e:
            self.printForward()
            self.printBackward()
            raise

    def removeFront(self):
        try:
            print("Remove F called")
            self.printForward()
            if self.head.next == self.tail:
                return None

            node = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

            self.printForward()
            print("Remove F End")
            return node
        except Exception as e:
            self.printForward()
            self.printBackward()
            raise

    def printForward (self):
        print("\nList Forward =>")
        temp = self.head
        while temp and temp != self.tail:
            temp = temp.next
            print(temp.val, end=",")

    def printBackward (self):
        print("\nList Backward =>")
        temp = self.tail
        while temp and temp != self.head:
            temp = temp.prev
            print(temp.val, end=",")

class LRUCache:

    def __init__(self, capacity: int):
        self.LRUOrderList = DoublyLinkedList()
        self.KeyMap = {}
        self.capacity=capacity
        self.curCapacity = 0

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
            self.curCapacity += 1
            if self.curCapacity > self.capacity:
                node1 = self.LRUOrderList.removeFront()
                if node1:
                    self.curCapacity -= 1
                    del self.KeyMap[node1.val[0]]
        else:
            node = self.KeyMap[key]
            self.LRUOrderList.removeNode(node)
            node.val = (key, value)
        self.LRUOrderList.insertRear(node)

        

        
