class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPosSpeed = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(carPosSpeed, reverse=True):
            timeToDest = (target - p) / s
            if not len(stack) or stack[-1] < timeToDest :
                stack.append(timeToDest)

        return len(stack)
        

        