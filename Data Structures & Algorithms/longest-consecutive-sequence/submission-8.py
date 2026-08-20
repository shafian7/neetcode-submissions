class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numSet = set(nums)

        for num in nums:
            if not num - 1 in numSet:
                currLength = 1
                while num + 1 in numSet:
                    currLength += 1
                    num += 1
                if currLength > longest:
                    longest = currLength
        
        return longest