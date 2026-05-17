from enum import Enum

class TokenType(Enum):
    VALUE = 0
    DIV_MUL_OPERATOR=1
    ADD_SUB_OPERATOR=2

class Token:
    def __init__(self, tokenType: TokenType, value: str):
        self.tokenType = tokenType
        self.value = value

class Solution:
    operationLambdas = {
        "+": lambda x,y: x + y,
        "-": lambda x,y: x - y,
        "/": lambda x,y: int(x / y) if y!=0 else float("INF"),
        "*": lambda x,y: x * y
    }
    def extractNumber (self, expr):
        count = 0
        value = ""

        while count < len(expr) and expr[count] in "0123456789":
            value += expr[count]
            count += 1

        return value, count

    def tokenizeExpression (self, s):
        tokenList = []
        i = 0
        while i < len(s):
            if s[i] in "+-":
                tokenList.append(Token(TokenType.ADD_SUB_OPERATOR, s[i]))
            elif s[i] in "/*":
                tokenList.append(Token(TokenType.DIV_MUL_OPERATOR, s[i]))
            elif s[i] in "0123456789":
                value, count = self.extractNumber(s[i:])
                i += count - 1
                tokenList.append(Token(TokenType.VALUE, value))
            i += 1

        return tokenList

    def evaluateOperations(self, tokens, opType: TokenType):
        if opType == TokenType.VALUE:
            return None

        stack = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.tokenType != opType:
                stack.append(token)
            else:
                prevToken = stack.pop()
                nextToken = tokens[i + 1]
                result = Solution.operationLambdas[token.value](int(prevToken.value), int(nextToken.value))
                stack.append(Token(TokenType.VALUE, str(result)))
                i += 1
            i += 1
        return stack


    def calculate(self, s: str) -> int:
        tokens = self.tokenizeExpression(s)
        tokens = self.evaluateOperations(tokens, TokenType.DIV_MUL_OPERATOR)
        tokens = self.evaluateOperations(tokens, TokenType.ADD_SUB_OPERATOR)

        return int(tokens[0].value)

        

        
        