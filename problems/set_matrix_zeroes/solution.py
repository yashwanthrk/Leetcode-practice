class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        def set_matrix_zeroes(r_, c_):
            for r in range(rows):
                for c in range(cols):
                    if r == r_ and matrix[r][c] != 0:
                        matrix[r][c] = 'X' 
                    if c == c_ and matrix[r][c] != 0:
                        matrix[r][c] = 'X' 


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    set_matrix_zeroes(r, c)
                else:
                    continue
    
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 'X':
                    matrix[r][c] = 0

           