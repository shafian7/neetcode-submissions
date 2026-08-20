class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in pairs:
                return [pairs[difference], i]
            else:
                pairs[nums[i]] = i
        
        