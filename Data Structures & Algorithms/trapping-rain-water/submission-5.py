class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        left, rigth = 0, len(height) - 1
        water = 0
        
        while left < rigth:
            if height[left] <= height[rigth]:
                if maxL - height[left] > 0:
                    water += maxL - height[left]
                if height[left] > maxL:
                    maxL = height[left]
                left += 1
            else:
                if maxR - height[rigth] > 0:
                    water += maxR - height[rigth]
                if height[rigth] > maxR:
                    maxR = height[rigth]
                rigth -= 1
        return water