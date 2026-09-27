class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for index, number in enumerate(nums):
            if number not in seen:
                seen[number] = []

            seen[number].append(index)

        left = 0
        right = 1

        for unique_number in seen:
            
            if len(seen[unique_number]) < 2:
                continue
            
            while right < len(seen[unique_number]):
                if abs(seen[unique_number][left] - seen[unique_number][right]) <= k:
                    return True
                
                left += 1
                right += 1

        return False