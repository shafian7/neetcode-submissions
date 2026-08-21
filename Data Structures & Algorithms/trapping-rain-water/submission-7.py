class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = [0] * len(height)
        ml = 0
        for i in range(len(height)):
            maxLeft[i] = ml
            if height[i] > ml:
                ml = height[i]
    
        maxRight = [0] * len(height)
        mr = 0
        for i in range(len(height) - 1, -1 , -1):
            maxRight[i] = mr
            if height[i] > mr:
                mr = height[i]
        
        res = 0

        for i in range(len(height)):
            res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        

        return res

            

        