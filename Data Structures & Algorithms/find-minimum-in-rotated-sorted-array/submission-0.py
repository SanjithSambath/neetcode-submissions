class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lower = 0
        upper = len(nums) - 1

        while lower < upper:
            middle = (lower + upper) // 2

            if nums[middle] > nums[upper]:
                lower = middle + 1   # minimum must be to the right
            else:
                upper = middle       # middle could be the minimum

        return nums[lower]