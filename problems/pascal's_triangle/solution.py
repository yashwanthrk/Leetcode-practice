class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * x for x in range(1, numRows + 1)]

        for row in range(2, numRows):
            for col in range(1, len(result[row]) - 1):
                result[row][col] = (
                    result[row - 1][col - 1] + result[row - 1][col]
                )
        return result
