from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if (k == len(arr)):
            return arr

        n = len(arr)
        if x <= arr[0]:
            return arr[:k]
        
        if x >= arr[-1]:
            return arr[n - k:]

        nearestElemIndex = self.findNearestElems(arr, x)

        result = deque()
        result.append(arr[nearestElemIndex])
        k -= 1

        l, r = nearestElemIndex - 1, nearestElemIndex + 1

        while k > 0:
            l_candidate = float("inf") if l < 0 else arr[l]
            r_candidate = float("inf") if l >= n else arr[r]

            if abs(l_candidate - x) > abs(r_candidate - x):
                r += 1
                nextElem = r_candidate
            else:
                l -= 1
                nextElem = l_candidate

            if nextElem >= x:
                result.append(nextElem)
            else:
                result.appendleft(nextElem)

            
            k -= 1

        return list(result)

        

    def findNearestElems (self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= target and mid != len(arr) - 1 and arr[mid + 1] >= target:
                return mid if abs(target - arr[mid]) < abs(target - arr[mid+1]) else mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        




# import heapq
# import math
# from collections import deque
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         if (k == len(arr)):
#             return arr
        
#         heap = [(abs(x - num), num) for num in arr]
#         heapq.heapify(heap)

#         result = deque ()
#         while k > 0:
#             _, elem = heapq.heappop(heap)
#             if elem >= x:
#                 result.append(elem)
#             else:
#                 result.appendleft(elem)
#             k -= 1

#         return list(result)