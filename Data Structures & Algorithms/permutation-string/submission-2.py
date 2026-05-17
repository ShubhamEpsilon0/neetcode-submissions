
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charRequiredFreq = Counter(s1)
        len_s1=len(s1)

        curCharRequiredFreq = dict(charRequiredFreq)
        L = 0
        for R in range(len(s2)):
            if s2[R] not in curCharRequiredFreq.keys():
                L = R + 1
                curCharRequiredFreq = dict(charRequiredFreq)
            else:
                curCharRequiredFreq[s2[R]] -= 1

                while min(curCharRequiredFreq.values()) < 0:
                    curCharRequiredFreq[s2[L]] += 1
                    L += 1
                if R - L + 1 == len_s1:
                    return True

        return False




    