class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        effective_time = time % (2 * (n - 1))
        
        position = 1
        direction = 1
        
        for _ in range(effective_time):
            position += direction
            
            if position == n:
                direction = -1
            elif position == 1:
                direction = 1
        
        return position