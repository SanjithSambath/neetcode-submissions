class Solution:
    def sortColors(self, nums: List[int]) -> None:

        zero_count = 0
        one_count = 0
        two_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
                
        i = 0

        for _ in range(zero_count):
            nums[i] = 0
            i += 1

        for _ in range(one_count):
            nums[i] = 1
            i += 1

        for _ in range(two_count):
            nums[i] = 2
            i += 1