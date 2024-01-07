class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(jobs)
        dp = [0] * n

        for i in range(n):
            # Find the last non-overlapping job using binary search
            lo, hi = 0, i - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if jobs[mid][0] <= jobs[i][1]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            # Calculate the maximum profit including or excluding the current job
            incl_profit = jobs[i][2] + (dp[hi] if hi >= 0 else 0)
            excl_profit = dp[i - 1] if i > 0 else 0

            # Update dp array with the maximum profit
            dp[i] = max(incl_profit, excl_profit)

        return dp[-1]