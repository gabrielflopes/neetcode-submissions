class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}

        for i in range(len(nums)):
            diferenca = target - nums[i]

            if diferenca in vistos:
                return [vistos[diferenca], i]
            
            vistos[nums[i]] = i

            