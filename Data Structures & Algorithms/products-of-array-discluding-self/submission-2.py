import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = math.prod(nums)
        output = []
        zero_count = 0

        for index, num in enumerate(nums): 

            if num == 0:
                zero_count = zero_count + 1

            if zero_count > 1:
                return [0]*len(nums)

            try:
                output.append(int(total_product/num))
            except ZeroDivisionError:
                nums[index] = 1 
                output.append(int(math.prod(nums)))
                nums[index] = 0

        return output