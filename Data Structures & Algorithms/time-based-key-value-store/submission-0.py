from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values:
            return ""

        index = self.FindLatestValHelper(values, timestamp)
        if index == -1:
            return ""
        return values[index][1]


    def FindLatestValHelper(self, values, target):
        #Do largest less than or equal to Bin Search
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = (low + high) // 2

            if (values[mid][0] == target) or (mid == len(values) - 1 and values[mid][0] < target) or (values[mid][0] < target and values[mid + 1][0] > target):
                return mid
            elif values[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


        
