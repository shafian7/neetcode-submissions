class Solution:
    def maxArea(self, heights: List[int]) -> int:

        largestArea = 0
        higher = len(heights) - 1

        lower = 0

        while lower < higher:

            area = (higher - lower) * min(heights[higher], heights[lower])
            largestArea = max(largestArea, area)
            if heights[lower] < heights[higher]:
                lower += 1
            else:
                higher -= 1
        
        return largestArea

        

