import heapq
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.childrens = {}
        self.sentenceIds = []

class Trie:
    def __init__(self, sentences, times):
        self.trieRoot = TrieNode("")
        self.sentenceMap = {}

        for sentence, time in zip(sentences, times):
            self.addSentence(sentence, time)

    def addSentence(self, sentence, times = 1):
        sentenceId = hash(sentence)
        if sentenceId not in self.sentenceMap:
            self.insertSentenceInTrie(sentence, sentenceId)

        sentence_times_pair = self.sentenceMap.get(sentenceId, [0, sentence])
        sentence_times_pair[0] -= times
        self.sentenceMap[sentenceId] = sentence_times_pair

    def insertSentenceInTrie(self, sentence, sentenceId):
        curNode = self.trieRoot
        curNode.sentenceIds.append(sentenceId)

        for char in sentence:
            if char not in curNode.childrens:
                curNode.childrens[char] = TrieNode(char)

            curNode = curNode.childrens[char]
            curNode.sentenceIds.append(sentenceId)

    class TrieIterator:
        def __init__(self, TrieInstance):
            self.curNode = TrieInstance.trieRoot

        def next(self, char):
            if char in self.curNode.childrens:
                self.curNode = self.curNode.childrens[char]
                return self.curNode
            
            return None



class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie(sentences, times)
        self.trieIterator = Trie.TrieIterator(self.trie)
        self.curStr = ""
        self.searchTrie = True
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trieIterator = Trie.TrieIterator(self.trie)
            self.trie.addSentence(self.curStr)
            self.curStr = ""
            self.searchTrie = True
            return []

        self.curStr += c
        node = None
        if self.searchTrie:
            node = self.trieIterator.next(c)
        if node is None:
            self.searchTrie = False
            return []

        sentence_time_pairs = [self.trie.sentenceMap[sid] for sid in node.sentenceIds]
        sentence_time_pairs.sort()

        return [item[1] for item in sentence_time_pairs[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
