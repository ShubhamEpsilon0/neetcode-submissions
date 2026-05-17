class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return str(sorted(list(s))) == str(sorted(list(t)))
        