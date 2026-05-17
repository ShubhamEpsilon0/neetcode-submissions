class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.candidatesLen = len(candidates)
        self.cache = {}
        ans = self.dp(0, target)

        return ans if ans else []

    def dp(self, curIndex, remainingTarget):
        if remainingTarget == 0:
            return [[]]

        if curIndex >= self.candidatesLen:
            return None

        if remainingTarget < self.candidates[curIndex]:
            return None

        if (curIndex, remainingTarget) in self.cache:
            return self.cache[(curIndex, remainingTarget)]

        curElem = self.candidates[curIndex] 
        repeatCount = 0
        i = curIndex
        while i < self.candidatesLen and self.candidates[i] == curElem:
            i+=1
            repeatCount+=1

        ans = self.dp(curIndex + repeatCount, remainingTarget)
        ans = [] if not ans else ans
        
        for j in range(1, repeatCount + 1):

            temp_ans = self.dp(curIndex + repeatCount, remainingTarget - curElem * j)
            if not temp_ans:
                continue

            temp_ans = self.appendSubSolutions([curElem] * j,temp_ans)
            ans.extend(temp_ans)

        self.cache[(curIndex, remainingTarget)] = ans
        return ans if ans else None

    def appendSubSolutions(self, curSelection, subSolution):
        res = []
        for sol in subSolution:
            r = list(curSelection)
            r.extend(sol)
            res.append(r)
        return res



            



        
        