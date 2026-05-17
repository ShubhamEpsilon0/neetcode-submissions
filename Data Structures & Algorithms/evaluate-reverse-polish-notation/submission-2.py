class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operationLambdas = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: int(x / y),
        }
        for token in tokens:
            if token in "+-*/":
                y = stack.pop()
                x = stack.pop()
                stack.append(operationLambdas[token[0]](x, y))
            else:
                stack.append(int(token))
            # print(stack)
        return stack[0]
                
        