class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        lower = max(weights)  # must fit the heaviest package
        upper = sum(weights)  # can ship everything in one day
        answer = upper 

        while lower <= upper:
            capacity = lower + (upper - lower) // 2

            days_used = 1
            load = 0

            for weight in weights:
                if load + weight > capacity:
                    days_used += 1
                    load = 0
                load += weight

            if days_used <= days:
                upper = capacity - 1  # works; try a smaller ship
            else:
                lower = capacity + 1  # too small; try a larger ship

        return lower

        