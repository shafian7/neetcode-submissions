class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            target2 = target - nums[i]
            new_nums = nums[:i] + nums[i+1:]
            if target2 in new_nums:
                j = new_nums.index(target2) + 1
                break
        return [i, j]
        