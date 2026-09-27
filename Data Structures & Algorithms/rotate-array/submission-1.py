class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k %= n
        moved = 0

        for start in range(n):
            if moved == n:
                break

            current = start
            value = nums[start]

            while True:
                next_index = (current + k) % n

                # Put value in its destination; carry away what was there.
                nums[next_index], value = value, nums[next_index]

                current = next_index
                moved += 1

                if current == start:
                    break