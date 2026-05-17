class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSumMatrix = [[0] * (len(matrix[0]) + 1)]
        for i in range(len(matrix)):
            self.prefixSumMatrix.append([0])
            curSum = 0
            for j in range(len(matrix[0])):
                curSum += matrix[i][j]
                self.prefixSumMatrix[-1].append(self.prefixSumMatrix[-2][j + 1] + curSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1 # for an extra row in prefix sum
        col1 += 1
        col2 += 1
        topRectSum = self.prefixSumMatrix[row1-1][col2]
        leftRectSum = self.prefixSumMatrix[row2][col1 - 1]
        topLeftCorner = self.prefixSumMatrix[row1-1][col1-1]
        return self.prefixSumMatrix[row2][col2] - topRectSum - leftRectSum + topLeftCorner

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)