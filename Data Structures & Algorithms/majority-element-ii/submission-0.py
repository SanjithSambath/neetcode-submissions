class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        output = []

        for number in nums:

            if number not in freq:
                freq[number] = 0
            
            freq[number] += 1

        for number in freq:
            if freq.get(number) > (len(nums)/3):
                output.append(number)

        return(output)