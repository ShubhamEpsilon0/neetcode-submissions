
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charRequiredFreq = Counter(s1)

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

                print(curCharRequiredFreq)
                if sum(curCharRequiredFreq.values()) == 0:
                    return True

        return False




    