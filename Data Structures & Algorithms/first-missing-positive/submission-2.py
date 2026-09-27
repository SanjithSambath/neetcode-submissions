class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = list(set(nums))
        nums = [x for x in nums if x > 0]
        nums = sorted(set(nums))

        if 1 not in nums or len(nums) == 0:
            return 1

        starting = nums[0]

        print(f'sorted is: {nums}')
        print(f'smallest = {starting}')

        for index, number in enumerate(nums):

            print(f'index = {index}, and number = {number}')

            print(index+starting)

            if number != (index + starting):
                print('yes')
                return index+1

        return (nums[-1] + 1)