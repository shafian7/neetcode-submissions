class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numSet = set(nums)

        while numSet:
            up = numSet.pop()
            currLength = 1
            down = up
            while down - 1 in numSet:
                currLength += 1
                down -= 1
                numSet.remove(down)
            while up + 1 in numSet:
                currLength += 1
                up += 1
                numSet.remove(up)
            if currLength > longest:
                longest = currLength
        
        return longest