class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1          # Last valid value in nums1
        j = n - 1          # Last value in nums2
        write = m + n - 1  # Last slot in nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1

            write -= 1