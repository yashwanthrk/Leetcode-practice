class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        def search_word(r, c, index):
            # Boundary check and character match
            if r < 0 or r >= ROW or c < 0 or c >= COL or board[r][c] != word[index]:
                return False

            # Base case: last character matches
            if index == len(word) - 1:
                return True

            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "0"

            # Explore all 4 possible directions
            exists = (
                search_word(r + 1, c, index + 1) or
                search_word(r - 1, c, index + 1) or
                search_word(r, c + 1, index + 1) or
                search_word(r, c - 1, index + 1)
            )

            # Restore the cell's original value
            board[r][c] = temp
            return exists

        # Iterate through the grid to find the starting point
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0] and search_word(r, c, 0):
                    return True

        return False



        
