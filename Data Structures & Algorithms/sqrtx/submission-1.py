class Solution:
    def mySqrt(self, x: int) -> int:

        bottom = 0 
        top = x

        while bottom <= top:
            middle = bottom + (top - bottom) // 2

            if x == middle**2:
                return middle
            
            if x > middle**2: 
                bottom = middle + 1
            
            if x < middle**2:
                top = middle - 1
            
        return bottom-1
            
        