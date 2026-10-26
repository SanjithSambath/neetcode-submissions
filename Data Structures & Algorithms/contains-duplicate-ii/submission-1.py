class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for index, number in enumerate(nums):

            if number not in seen:
                seen[number] = []
                
            seen[number].append(index)
            
            if len(seen[number]) > 1:
                if abs(seen[number][-1] - seen[number][-2]) <= k:
                    return True
                
        else:
            return False
