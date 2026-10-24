class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        diferenca = 0

        for i, num in enumerate(numbers):
            diferenca = target - num

            if diferenca in seen:
                return [seen[diferenca], i + 1]
            seen[num] = i + 1