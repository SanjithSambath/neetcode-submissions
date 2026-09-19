import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = math.prod(nums)
        output = []

        for index, num in enumerate(nums): 
            try:
                output.append(int(total_product/num))
            except:
                nums[index] = 1
                output.append(int((math.prod(nums))))
                nums[index] = 0

        return output