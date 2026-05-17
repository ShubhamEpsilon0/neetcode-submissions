class CountSquares:

    def __init__(self):
        self.xIndexedPoints = defaultdict(set)
        self.pointsMap = defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.xIndexedPoints[point[0]].add(tuple(point))
        self.pointsMap[tuple(point)] += 1

    def countSquareFrom2Points(self, p1, p2):
        dist = abs(p2[1] - p1[1])
        #if p3 -> (p1[0] + dist, p1[1]) and p4 -> (p1[0] + dist, p1[1] + dist) they exist count square
        count = 0
        p3 = (p1[0] + dist, p1[1])
        p4 = (p2[0] + dist, p2[1])

        if p3 in self.pointsMap and p4 in self.pointsMap:
            count += self.pointsMap[p2] * self.pointsMap[p3] * self.pointsMap[p4]

        p3 = (p1[0] - dist, p1[1])
        p4 = (p2[0] - dist, p2[1])

        if p3 in self.pointsMap and p4 in self.pointsMap:
            count += self.pointsMap[p2] * self.pointsMap[p3] * self.pointsMap[p4]

        return count


    def count(self, point: List[int]) -> int:

        pointsWithSameX = self.xIndexedPoints[point[0]]
        sq_count = 0
        for pts in pointsWithSameX:
            if pts[1] != point[1]:
                sq_count += self.countSquareFrom2Points(point, pts)

        return sq_count

        


        
