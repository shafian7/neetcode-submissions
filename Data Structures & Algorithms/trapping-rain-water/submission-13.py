class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        
        res = 0

        mr = height[right]
        ml = height[left]
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
        while left < right:
            if height[left] > ml:
                ml = height[left]
            elif height[right] > mr:
                mr = height[right]
            else:
                res += max(min(mr, ml) - height[left], min(mr, ml) - height[right])

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

            

        