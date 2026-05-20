from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.stacks = [[]]

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        freq = self.frequency[val]
        
        if len(self.stacks) <= freq:
            self.stacks.append([])
        
        self.stacks[freq].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        self.frequency[val] -= 1
        return val

