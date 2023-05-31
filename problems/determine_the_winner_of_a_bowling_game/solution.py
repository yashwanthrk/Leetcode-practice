class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(nums):
            score = 0
            flag = False

            for i in range(len(nums)):
                score += nums[i]

                if flag:
                    score += nums[i]
                    doubles -= 1

                    if doubles == 0:
                        flag = False

                if nums[i] == 10:
                    doubles = 2
                    flag = True
                    
            return score
        
        score1, score2 = score(player1), score(player2)
        
        if score1 == score2:
            return 0
        elif score1 > score2:
            return 1
        else:
            return 2