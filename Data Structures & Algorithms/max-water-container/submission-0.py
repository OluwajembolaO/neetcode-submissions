class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = 0
        l = 0 
        r = len(heights) -1 
        while l < r:
            if (maxH < ((r-l) * min(heights[l], heights[r]))):
                maxH = ((r-l) * min(heights[l], heights[r]))
                print(maxH)
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r -=1 
            else: 
                l += 1
                r -= 1
        return maxH
        