from collections import defaultdict

class FreqStackMetaData:
    def __init__(self):
        self.freq = 0
        self.stack = []

    def addInstance(self, pos):
        self.freq += 1
        self.stack.append(pos)

    def removeInstance(self):
        self.freq -= 1
        self.stack.pop()

    def __lt__(self, other):
        if self.freq < other.freq:
            return True 
        elif self.freq > other.freq:
            return False
        else:
            return self.stack[-1] < other.stack[-1]


class FreqStack:

    def __init__(self):
        self.valFreqMap = defaultdict(FreqStackMetaData)
        self.elemCount = 0
        
    def push(self, val: int) -> None:
        self.valFreqMap[val].addInstance(self.elemCount)
        self.elemCount += 1

    def pop(self) -> int:
        maxItem = max([(freq_stack_meta_data, val) for val, freq_stack_meta_data in self.valFreqMap.items()])
        self.valFreqMap[maxItem[1]].removeInstance()
        if not self.valFreqMap[maxItem[1]].stack:
            del self.valFreqMap[maxItem[1]]

        return maxItem[1]
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()