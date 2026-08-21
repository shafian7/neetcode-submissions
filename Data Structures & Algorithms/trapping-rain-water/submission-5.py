class Solution:
    def trap(self, height: List[int]) -> int:

        for i in range(len(height)):
            if height[i] > 0:
                lower = i
                break
            if i == len(height) - 1 and height[i] == 0:
                return 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > 0:
                upper = i
                break
        
        

        largestLower = 0
        largestUpper = 0
        res = 0

        while lower < upper:
            
            if height[lower] > largestLower:
                largestLower = height[lower]
            if height[upper] > largestUpper:
                largestUpper = height[upper]
            else:
                res += max(min(largestLower, largestUpper) - height[lower], min(largestLower, largestUpper) - height[upper], 0)

            if height[lower] < height[upper]:
                lower += 1
            else:
                upper -= 1

        return res
            

        
            

        