class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total_max = 0
        for row in accounts:
            max = 0
            for money in row:
                max += money
                if max > total_max:
                    total_max = max

        return total_max