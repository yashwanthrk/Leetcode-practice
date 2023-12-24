class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        

        rows = len(mat)
        cols = len(mat[0])

        def check_for_special_postion(r_, c_):
            for r in range(rows):
                for c in range(cols):
                    
                    if r == r_  and c == c_:
                        continue

                    if r == r_ and mat[r][c] != 0:
                        return False  
                    if c == c_ and mat[r][c] != 0:
                        return False

            return True

          


        count = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    print(r, c)
                    if check_for_special_postion(r, c):
                        count += 1
            

        
        return count
