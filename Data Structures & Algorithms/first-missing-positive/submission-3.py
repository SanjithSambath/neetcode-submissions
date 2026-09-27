class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = set(nums)

        for i in range(len(nums) + 1):
            i = i + 1

            if i not in nums:
                return i
