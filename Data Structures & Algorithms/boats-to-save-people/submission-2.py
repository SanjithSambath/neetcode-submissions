class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        total_boats = 0

        left = 0
        right = len(people)-1

        people = sorted(people)

        while left <= right:

            if (people[left] + people[right]) <= limit:

                print(f'double: left = {left} and right = {right}')

                total_boats += 1
                left += 1
                right -= 1
            
            if (people[left] + people[right]) > limit:

                print(f'single: left = {left} and right = {right}')

                total_boats += 1
                right -= 1
            
        return total_boats