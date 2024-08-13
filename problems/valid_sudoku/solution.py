class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num != '.':
                    
                    if num in rows[i]:
                        return False

                    if num in columns[j]:
                        return False
                    
                    # Calculate the index for the 3x3 box
                    box_index = (i // 3) * 3 + j // 3

                    if num in boxes[box_index]:
                        return False
                    
                    rows[i].add(num)
                    columns[j].add(num)
                    boxes[box_index].add(num)
        
        return True
