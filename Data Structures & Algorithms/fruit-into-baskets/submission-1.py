class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 0:
            return 0

        maxFruits = 0
        start = 0
        selected_fruits = {fruits[0]: 0}

        for end in range(1, len(fruits)):
            if fruits[end] not in selected_fruits and len(selected_fruits) == 2:
                maxFruits = max(maxFruits, end - start)
                fruit_to_remove = list(set(selected_fruits.keys()) - set([fruits[end - 1]]))[0]
                start = selected_fruits[fruit_to_remove] + 1
                del selected_fruits[fruit_to_remove]

            selected_fruits[fruits[end]] = end

        maxFruits = max(maxFruits, len(fruits) - start)

        return maxFruits

        