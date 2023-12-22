class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

          # Find the transpose of the matrix
        # Reverse the rows of the matrix

       #transpose 
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                # visualize it with diagram - it will be easy

                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
       
        print(matrix)
       
        #reverse
        for row in matrix:
            row.reverse()