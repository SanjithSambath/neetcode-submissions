class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for index, number in enumerate(numbers):

            complement = target - number

            if complement in seen:
                return [seen[complement], index + 1]

            seen[number] = index + 1