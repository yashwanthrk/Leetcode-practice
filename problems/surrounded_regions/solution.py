class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board:
            return 0

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != 'O':
                    return

            board[i][j] = '#'

            # explore the cell below the current cell.        
            dfs(i+1, j) 
            # explore the cell above the current cell.
            dfs(i-1, j)
            # explore the cell to the right of the current cell.        
            dfs(i, j+1)
            # explore the cell to the left of the current cell.
            dfs(i, j-1)


        # capture unsurounded region  ('O' -> '#')
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)
        

        # capture surrounded region ('O' -> 'X')
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'


        #  change unsurrounded region back to 'O' i.e ( '#' -> 'O' )
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'