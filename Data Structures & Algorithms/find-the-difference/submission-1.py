from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(dict(Counter(t) - Counter(s)).keys())[0]
        