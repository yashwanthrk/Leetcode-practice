class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    
        #transpose 
        for row in range(len(matrix)):
            for col in range(row,len(matrix)):
                # print(row, col)
                # visualize it with diagram - it will be easy

                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        #reverse
        for row in matrix:
            row.reverse()

       
       
       
        # output  = [[0 for _ in (row)] for row in (matrix)]
        # # transpose matrix
        # # iterate through rows
        # for i in range(len(matrix)):
        # # iterate through columns
        #     for j in range(len(matrix[0])):
        #         output[j][i] = matrix[i][j]
        
        # # print(output)


        # for row in output:
        #     row.reverse()
        # print(output)

        # matrix =  output


   
 