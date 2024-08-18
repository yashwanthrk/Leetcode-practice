class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x, y, index):

            # If all characters matched
            if index == len(word):  
                return True    

            # Check if the current position is out of bounds
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            
          

            # Check if the current cell does not match the current character in the word
            if board[x][y] != word[index]:
                return False
            
          
            
            # Mark the cell as visited
            temp = board[x][y]
            board[x][y] = '#'
            
            if (dfs(x + 1, y, index + 1) or
                dfs(x - 1, y, index + 1) or
                dfs(x, y + 1, index + 1) or
                dfs(x, y - 1, index + 1)):
                return True
            
            # Restore the original value
            board[x][y] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # Start DFS if the first letter matches
                    if dfs(i, j, 0):  
                        return True
        
        return False