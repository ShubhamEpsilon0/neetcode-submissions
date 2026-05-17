from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.constructAdjList(wordList)
        print(self.adjList)
        self.beginWord = beginWord
        self.endWord = endWord

        return self.buildWordLadder()


    def buildWordLadder (self):
        bfsQueue = [self.beginWord]
        visited = set()
        bfsDepthCount = 2
        wordLength = len(self.beginWord)

        while bfsQueue:
            newQueue = []
            print(bfsQueue)
            while bfsQueue:
                curWord = bfsQueue.pop()
                visited.add(curWord)
                # get neighbors
                neighbors = set()
                for i in range(wordLength):
                    key = curWord[:i] + "*" + curWord[i+1:]
                    neighbors.update(set(self.adjList[key]))

                for neighbor in neighbors:
                    if neighbor == self.endWord:
                        return bfsDepthCount
                    if neighbor not in visited:
                        newQueue.append(neighbor)

            bfsDepthCount += 1
            bfsQueue = newQueue
        
        return 0

    def constructAdjList(self, wordList):
        self.adjList = defaultdict(list)

        wordLength = len(wordList[0])
        for i in range(wordLength):
            for word in wordList:
                key = word[:i] + "*" + word[i+1:]
                self.adjList[key].append(word)



        