class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        maxArea = 0
        while left < right:
            #we find the minHeight
            minHeight = min(heights[left], heights[right])
            if minHeight == heights[left]:
                left+=1
            else:
                right-=1
            #then we calculate the area and find the maxArea
            area = minHeight * (right-left+1)
            maxArea = max(maxArea, area)
        return max(maxArea, area)

