class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        bottom = 0 
        top = len(nums) - 1

        while bottom <= top:
            middle = bottom + (top - bottom) // 2

            if target == nums[middle]:
                return middle
            
            if target > nums[middle]: 
                bottom = middle + 1
            
            if target < nums[middle]:
                top = middle - 1
            
        return bottom
            
        