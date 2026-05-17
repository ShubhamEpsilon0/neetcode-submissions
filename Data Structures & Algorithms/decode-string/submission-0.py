class StringIterator:
    def __init__(self, s):
        self.str = s
        self.index = 0
        self.len = len(s)

    def peek(self):
        return self.str[self.index]

    def next(self):
        self.index+=1

    def prev(self):
        self.index -=1

    def hasNext(self):
        return self.index != self.len

    def hasPrev(self):
        return self.index != 0





class Solution:
    def decodeString(self, s: str) -> str:
        str_iter = StringIterator(s)
        return self.decode(str_iter)

    def extractRepetition(self, str_iter):
        count = 0
        while str_iter.peek() in "0123456789":
            count = count * 10 + int(str_iter.peek())
            str_iter.next()

        return count


    def decode(self, str_iter):
        ans = ""
        count = 0
        while str_iter.hasNext():
            peekChar = str_iter.peek()
            if peekChar in "0123456789":
                count = self.extractRepetition(str_iter)
            elif peekChar in "[":
                str_iter.next()
                decoded_str = self.decode(str_iter)
                ans += decoded_str * count
                count = 0
            elif peekChar == "]":
                str_iter.next()
                return ans
            else:
                str_iter.next()
                ans += peekChar

        return ans



        