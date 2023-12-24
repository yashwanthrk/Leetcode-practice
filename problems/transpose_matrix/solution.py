class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        

#         This code assumes that the number of rows in the original matrix is equal to the number of columns in the transposed matrix, and vice versa. If this assumption doesn't hold (i.e., if the original matrix is not square), you may encounter an "index out of range" error.

# To fix this issue, you should use the dimensions of the transposed matrix when iterating. 

        
        rows = len(matrix)
        cols = len(matrix[0])
        
        new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]


        for r in range(rows):
            for c in range(cols):
                new_matrix[c][r] = matrix[r][c]
        

        return new_matrix
