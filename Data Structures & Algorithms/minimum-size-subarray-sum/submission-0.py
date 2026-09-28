class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        shortest_window = len(nums) + 1 # init the shortest window to somethign not possible

        left = 0 
        right = 0 
        total = 0

        while right < len(nums):

            total += nums[right]

            while total >= target:
                length = right - left + 1

                total -= nums[left]
                left += 1

                shortest_window = min(shortest_window, length)

            right += 1
        
        if (shortest_window == len(nums) + 1):
            return 0
        else: 
            return shortest_window