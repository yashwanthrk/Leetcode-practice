class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                if matrix[r][c] == target:
                    return True

                if matrix[r][c] > target:
                    return False
                

        return False
        