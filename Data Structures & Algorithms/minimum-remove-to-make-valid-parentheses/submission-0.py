class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openParenthesisStack = []
        ans = ""
        j = 0
        for i in range(len(s)):
            if s[i] == "(":
                openParenthesisStack.append(j)
            elif s[i] == ")":
                if not openParenthesisStack:
                    continue
                openParenthesisStack.pop()

            ans += s[i]
            j += 1

        openParenthesisStack = set(openParenthesisStack)
        f_ans = ""
        for i in range(len(ans)):
            if i in openParenthesisStack:
                continue

            f_ans += ans[i]

            

        return f_ans
            
        