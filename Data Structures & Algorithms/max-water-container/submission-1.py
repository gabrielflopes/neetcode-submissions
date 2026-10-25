class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, rigth = 0, len(heights) - 1
        best = 0
        area = 0

        while left < rigth:
            area = ((rigth - left) * min(heights[left], heights[rigth]))
            best = max(area, best)

            if heights[left] < heights[rigth]:
                left += 1
            else:
                rigth -= 1
        return best
            
        
            



#choose two bars
#max amount of water 
#area = (heights[X] - heights[Y] * min(heights[X], heights[Y]))
#max water = max(best, area)
