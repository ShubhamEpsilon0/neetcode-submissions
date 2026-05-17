class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.numToCharsMap = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz",
        }
        self.digits = digits
        self.ans = []
        self.bt(0, "")
        return self.ans

    def bt(self, index, curCombination):
        if index == len(self.digits):
            self.ans.append(curCombination)
            return

        for ch in self.numToCharsMap[self.digits[index]]:
            self.bt(index + 1, curCombination + ch)

        