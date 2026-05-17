class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asteriskStack = []

        for i, ch in enumerate(s):
            if ch == "*":
                asteriskStack.append(i)
                continue

            if ch == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif asteriskStack:
                    asteriskStack.pop()
                else:
                    return False

        while stack:
            if asteriskStack and asteriskStack[-1] > stack[-1]:
                stack.pop()
                asteriskStack.pop()
            else:
                return False

        return True
        