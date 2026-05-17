class TrieNode:
    def __init__(self, val):
        self.val = val
        self.isWordEnd = False
        self.children = {}

    def addChild(self, character):
        self.children[character] = TrieNode(character)

class TrieSearchIterator:
    def __init__(self, trie):
        self.trie = trie
        self.curNode = trie.root
        self.pathHistory = []


    def nextChar(self, char):
        if char not in self.curNode.children:
            return False

        self.pathHistory.append(self.curNode)
        self.curNode = self.curNode.children[char]
        return True

    def isAtWordEnd(self):
        return self.curNode.isWordEnd

    def back(self):
        if self.curNode == self.trie.root:
            return False

        self.curNode = self.pathHistory.pop()
        return True

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insertWord(self, word):
        curNode = self.root

        for ch in word:
            if ch not in curNode.children:
                curNode.addChild(ch)
            curNode = curNode.children[ch]

        curNode.isWordEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.ans = set()

        for word in words:
            self.trie.insertWord(word)

        self.n = len(board)
        self.m = len(board[0])

        self.board = board

        for i in range(self.n):
            for j in range(self.m):
                trieIterator = TrieSearchIterator(self.trie)
                visited = set ()
                curChars = list()
                self.findWordRecur(visited, trieIterator, i, j, curChars)

        return list(self.ans)
        
        

    def findWordRecur(self, visited, iterator, r, c, curChars):
        if r < 0 or r >= self.n or c < 0 or c >= self.m:
            return

        if not iterator.nextChar(self.board[r][c]):
            return

        visited.add((r,c))
        curChars.append(self.board[r][c])

        if iterator.isAtWordEnd():
            self.ans.add("".join(curChars))

        dirs = [(1, 0), (-1, 0), (0,1), (0, -1)]

        for dr,dc in dirs:
            if (r+dr, c+dc) not in visited:
                self.findWordRecur(visited, iterator, r + dr, c + dc, curChars)

        curChars.pop()
        iterator.back()
        visited.remove((r,c))




        




        


        