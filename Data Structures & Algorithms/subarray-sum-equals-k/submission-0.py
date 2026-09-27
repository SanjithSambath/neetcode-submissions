class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sums = {0: 1}  # Sum before the array starts
        running_sum = 0
        answer = 0

        for number in nums:
            running_sum += number

            needed = running_sum - k
            if needed in seen_sums:
                answer += seen_sums[needed]

            if running_sum not in seen_sums:
                seen_sums[running_sum] = 0
            seen_sums[running_sum] += 1

        return answer