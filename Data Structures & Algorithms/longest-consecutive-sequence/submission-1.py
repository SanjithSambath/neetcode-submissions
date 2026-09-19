class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest_yet = 0
        
        for num in seen:
            if (num-1) not in seen: #if there is no prelude

                i = num
                potential_longest = 0

                while (i in seen):
                    potential_longest = potential_longest + 1 
                    i = i+1
                
                if potential_longest > longest_yet:
                    longest_yet = potential_longest

        return longest_yet