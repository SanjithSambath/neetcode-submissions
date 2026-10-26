class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        bottom = 0 
        top = (len(matrix[0])) * len(matrix) - 1
        
        while bottom <= top:
            middle = bottom + (top - bottom) // 2

            row = middle // len(matrix[0])
            col = middle % len(matrix[0])

            if target == matrix[row][col]:
                return True
            
            if target > matrix[row][col]: 
                bottom = middle + 1
            
            if target < matrix[row][col]:
                top = middle - 1
            
        return False
            
        