class Solution:
    def trap(self, height: List[int]) -> int:

        max_index = height.index(max(height))

        total = 0

        left_max = height[0]

        for i in range(1, max_index):

            if height[i] >= left_max:
                left_max = height[i]

            else:
                total += left_max - height[i]

        right_max = height[-1]

        for i in range(len(height) - 2, max_index, -1):

            if height[i] >= right_max:
                right_max = height[i]
                
            else:
                total += right_max - height[i]

        return total









        
        total = 0

        compute_list = []
        one_sided_total = 0

        ptr = 0

        while ptr < len(height):

            current_height = height[ptr]
            
            if len(compute_list) == 0: # should only run once
                if current_height > 0:
                    compute_list.append(current_height)
            
            else:

                compute_list.append(current_height)

                if current_height >= compute_list[0]:

                    total += one_sided_total
                    one_sided_total = 0

                    compute_list = [compute_list[-1]]

                else:
                    one_sided_total = one_sided_total + (compute_list[0] - current_height)

            ptr = ptr + 1

        return total