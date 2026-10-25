class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, rigth = i + 1, len(nums) - 1
            while left < rigth:
                soma = num + nums[left] + nums[rigth]

                if soma > 0:
                    rigth -= 1
                elif soma < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[rigth]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < rigth:
                        left += 1
                    
        return res
                    

        