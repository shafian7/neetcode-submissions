class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numSet = set(nums)

        for num in nums:
            if not num - 1 in numSet:
                currLength = 1
                while num + currLength in numSet:
                    currLength += 1
                longest = max(longest, currLength)
        
        return longest