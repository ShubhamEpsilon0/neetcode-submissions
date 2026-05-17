class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for pos in range(3):
            tripletFound = False
            for triplet in triplets:
                if triplet[pos] == target[pos]:
                    if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                        tripletFound = True
                        break
            if not tripletFound:
                return False

        return True
        