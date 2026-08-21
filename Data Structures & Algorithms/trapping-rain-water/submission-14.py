class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        
        res = 0

        mr = height[r]
        ml = height[l]
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        
        while l < r:
            if height[l] > ml:
                ml = height[l]
            elif height[r] > mr:
                mr = height[r]
            else:
                res += max(min(mr, ml) - height[l], min(mr, ml) - height[r])

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

            

        