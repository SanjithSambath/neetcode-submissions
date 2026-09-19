class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        int_freq_table = {}

        # Count frequencies
        for number in nums:
            if number not in int_freq_table:
                int_freq_table[number] = 0

            int_freq_table[number] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in int_freq_table.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets) - 1, 0, -1): # go backwards
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result
        