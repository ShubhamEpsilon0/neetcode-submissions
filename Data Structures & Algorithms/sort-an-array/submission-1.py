class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums

    def heapify(self, arr, rootIndex, length):
        largest = rootIndex

        leftChild = 2 * rootIndex
        rightChild = 2 * rootIndex + 1

        if leftChild < length and arr[leftChild] > arr[largest]:
            largest = leftChild

        if rightChild < length and arr[rightChild] > arr[largest]:
            largest = rightChild

        if largest != rootIndex:
            arr[largest], arr[rootIndex] = arr[rootIndex], arr[largest]

            self.heapify (arr, largest, length)

    def heapSort (self, arr):
        length = len(arr)

        for i in range(length // 2, -1, -1):
            self.heapify(arr, i, length)

        
        for i in range(length - 1, 0, -1):
            # Move current root to end
            arr[0], arr[i] = arr[i], arr[0]

            # Call max heapify on the reduced heap
            self.heapify(arr, 0, i)

        