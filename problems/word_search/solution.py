class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            if index == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (backtrack(r + 1, c, index + 1) or 
                     backtrack(r - 1, c, index + 1) or 
                     backtrack(r, c + 1, index + 1) or 
                     backtrack(r, c - 1, index + 1))
            
            board[r][c] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False