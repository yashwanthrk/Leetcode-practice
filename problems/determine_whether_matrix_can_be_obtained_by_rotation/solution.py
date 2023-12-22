class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        for i in range(4):
            if mat == target:
                return True
            else :
                #transposing the matrix
                for i in range(len(mat)) :
                    for j in range(i+1,len(mat)):
                        temp = mat[i][j]
                        mat[i][j] = mat[j][i]
                        mat[j][i] = temp
                #reversing the rows
                for i in range(len(mat)):
                    mat[i].reverse()
                print(mat)
        return False

        # def rotate_matrix(matrix):
            
        #     # transpose 
        #     for row in range(len(matrix)):
        #         for col in range(row, len(matrix[0])):
        #             temp = matrix[row][col]
        #             matrix[row][col] = matrix[col][row]
        #             matrix[col][row] = temp
        
        
        #     #reverse
        #     for row in matrix:
        #         row.reverse()

        # def are_matrices_equal(matrix1, matrix2):
        #     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        #         return False

        #     rows = len(matrix1)
        #     cols = len(matrix1[0])

        #     for i in range(rows):
        #         for j in range(cols):
        #             if matrix1[i][j] != matrix2[i][j]:
        #                 # Found a mismatch, matrices are not equal
        #                 return False

        #     return True
    
        

        # # max rotations 4 times
        # # including current state compare two matrices

        # for _ in range(4):
        #     rotate_matrix(mat)
        #     if are_matrices_equal(mat, target):
        #         return True
        
        # return False

    

