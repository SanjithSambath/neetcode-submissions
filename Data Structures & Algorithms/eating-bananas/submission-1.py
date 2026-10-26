class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        lower = max(1, (sum(piles) + h - 1) // h)
        upper = max(piles)
        answer = upper

        while lower <= upper:
            k = lower + (upper - lower) // 2
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k  # round up pile / k

                if hours > h:
                    break

            if hours > h:
                lower = k + 1  # too slow; try a higher speed
            else:
                answer = k     # works; remember it
                upper = k - 1  # try a lower speed

        return answer