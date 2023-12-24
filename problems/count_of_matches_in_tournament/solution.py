class Solution:
    def numberOfMatches(self, n: int) -> int:
        


        def count_matches(team, count):
            
           

            if team == 1:
                return count

            if team % 2 == 0:
                team = team // 2
                count += team

            else:
                team = ((team - 1) // 2) + 1
                count += team - 1



            return count_matches(team, count)
        


        return count_matches(n, 0)


