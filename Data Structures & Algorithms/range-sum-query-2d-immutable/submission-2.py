class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        sum_table = []
        additive_total = 0
        
        for row in matrix:
            for col in row:
                additive_total = additive_total + col
                sum_table.append(additive_total)

        self.sum_table = sum_table
        self.matrix = matrix

        print(sum_table)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 == col1 == row2 == col2 == 0:
            print('single element')
            return self.matrix[0][0]

        total = 0

        def convert(row, col):
            final = (len(self.matrix[0]) * row) + col
            return final
        
        converted_pos_1 = convert(row1, col1)
        converted_pos_2 = convert(row2, col2)

        for i in range(row2 - row1 + 1):

            converted_pos_1 = convert(row1 + i, col1)
            converted_pos_2 = convert(row1 + i, col2)

            total += (
                (self.sum_table[converted_pos_2]) - (self.sum_table[converted_pos_1]) 
                + (self.matrix)[i+row1][col1]
            )

            print(f'total: {total}')
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)gf 
