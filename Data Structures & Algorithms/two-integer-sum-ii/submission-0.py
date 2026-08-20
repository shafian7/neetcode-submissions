class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lower = 0
        upper = len(numbers) - 1

        while lower < upper:

            curr = numbers[upper] + numbers[lower]

            if curr == target:
                return [lower + 1, upper + 1]
            
            if target > curr:
                lower += 1
            if target < curr:
                upper -= 1
        
