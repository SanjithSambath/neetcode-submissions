class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        int_freq_table = {}
        top_freq_k = []
        top_freq_counts = []

        # Count frequencies
        for number in nums:
            if number not in int_freq_table:
                int_freq_table[number] = 0

            int_freq_table[number] += 1

        # Build top k
        for num, count in int_freq_table.items():

            # Find where this frequency should be inserted
            insert_index = 0

            while (
                insert_index < len(top_freq_counts)
                and top_freq_counts[insert_index] < count
            ):
                insert_index += 1

            top_freq_counts.insert(insert_index, count)
            top_freq_k.insert(insert_index, num)

            # If we now have more than k, remove smallest
            if len(top_freq_k) > k:
                top_freq_counts.pop(0)
                top_freq_k.pop(0)

        return top_freq_k