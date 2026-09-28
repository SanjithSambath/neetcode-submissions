class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)

        # binary search
        while left < right:
            middle = (left + right) // 2

            if arr[middle] < x:
                left = middle + 1
            else:
                right = middle

        pos = left

        # make the ptrs work regardlss if they r negative or not 
        left = pos - 1
        right = pos

        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]