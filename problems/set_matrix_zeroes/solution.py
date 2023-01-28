class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        zeroes_row = [False] * m
        zeroes_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True

        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
    
    
        
        # # output  = [[0 for _ in (row)] for row in (matrix)]
        
        # # for i in range(len(matrix)):
        # #     for j in range(len(matrix[i])):
        # #         output[i][j] = matrix[i][j]

        # # matrix copy
        # output = [row[:] for row in matrix]

        # def set_row_column_zeroes(i, j):   
        #     for row in range(len(matrix[i])):
        #         output[i][row] = 0
        
        #     for row in range(len(matrix)):
        #         output[row][j] = 0

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] != 0:
        #             continue

        #         # make all row and colums zeros
        #         set_row_column_zeroes(i, j)
                
        
        # matrix = [row[:] for row in output]

        # print(output, matrix)
