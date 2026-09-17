class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memory_hash = {}

        for index, number in enumerate(nums): 

            if (target - number) in memory_hash: 
                return [memory_hash[target-number], index]
            
            else: 
                memory_hash[number] = index