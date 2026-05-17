from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            anagramMap[self.encodeStr(s)].append(s)

        return list(anagramMap.values())

    def encodeStr(self, s):
        freqArr = [0]*26
        s = s.lower()
        for c in s:
            freqArr[ord(c) - 97]+=1
        return str(freqArr)
        