class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        


        ROWS = len(board)
        COLS = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtracking(r, c, index):
            
            if index == len(word):
                return False

            if not (0 <= r < ROWS and 0 <= c < COLS)  or board[r][c] != word[index]:
                return False


            if index == len(word) - 1:
                return True 

            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"  # Temporarily mark it as visited

            # Explore all four directions
            for dx, dy in directions:
                if backtracking(r + dx, c + dy, index + 1):
                    return True

            # Restore the cell value (backtrack)
            board[r][c] = temp
            return False

            

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    # start backtracking
                    if backtracking(r, c, 0):
                        return True

        
        return False

#         Time and Space Complexity

# The worst-case scenario involves visiting every cell for each character of the word.
# For a grid of size m × n and a word of length k, the complexity is O(m × n × 4^k), where 4^k comes from exploring 4 directions at each step.
# Space Complexity:

# The recursion depth is proportional to the length of the word, so the space complexity is O(k).
