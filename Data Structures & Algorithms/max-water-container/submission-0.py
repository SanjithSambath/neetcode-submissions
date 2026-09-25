class Solution:
    def maxArea(self, heights: List[int]) -> int:

        biggest_total = 0

        # height, index
        def compute(pair_1: tuple, pair_2: tuple): 

            height = min(pair_1[0], pair_2[0])
            width = abs(pair_1[1] - pair_2[1])

            total = height * width
            return total

        ptr_1 = 0 
        ptr_2 = len(heights)-1

        while ptr_1 != ptr_2:

            new_total = compute((heights[ptr_1], ptr_1), (heights[ptr_2], ptr_2))

            if new_total > biggest_total:
                biggest_total = new_total
            

            if heights[ptr_1] > heights[ptr_2]: 
                ptr_2 = ptr_2 - 1 

            else: 
                ptr_1 = ptr_1 + 1

        return biggest_total