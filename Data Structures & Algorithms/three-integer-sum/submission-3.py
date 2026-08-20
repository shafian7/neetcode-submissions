class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []

        curr = float("-inf")

        for i in range(len(nums) - 2):
            if nums[i] == curr:
                continue
            curr = nums[i]

            lower = i + 1
            higher  = len(nums) - 1
            target = 0 - curr
            while lower < higher:
                currSum = nums[lower] + nums[higher]
                if currSum == target:
                    res.append([curr, nums[lower], nums[higher]])
                    curr2 = nums[higher]
                    while higher >= 0 and nums[higher] == curr2:
                        higher -= 1
                    curr3 = nums[lower]
                    while lower < len(nums) and curr3 == nums[lower]:
                        lower += 1
                if currSum > target:
                    curr2 = nums[higher]
                    while higher >= 0 and nums[higher] == curr2:
                        higher -= 1
                if currSum < target:
                    curr3 = nums[lower]
                    while lower < len(nums) and curr3 == nums[lower]:
                        lower += 1
                
        return res
                




            


                