from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charRequired = Counter(ransomNote)
        charAvailable = Counter(magazine)

        for char, count in charRequired.items():
            if char not in charAvailable or charAvailable[char] < count:
                return False


        return True

        