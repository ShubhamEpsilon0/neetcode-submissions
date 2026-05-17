# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possibleCelebrity = -1

        for i in range(n):
            j = 0
            while j < n:
                if i != j and knows(i, j):
                    break
                j += 1
            if j == n:
                possibleCelebrity = i
                break

        for i in range(n):
            if not knows(i, possibleCelebrity):
                return -1

        return possibleCelebrity


        