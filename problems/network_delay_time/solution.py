from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Initialize delay times
        delay_time = [float('inf')] * (n + 1)
        delay_time[k] = 0  # Start node delay is 0
        
        # Step 2: Relax edges up to n-1 times
        for _ in range(n - 1):
            for src, dst, time in times:
                if delay_time[src] + time < delay_time[dst]:
                    delay_time[dst] = delay_time[src] + time
        
        # Step 3: Calculate the maximum delay
        max_delay = max(delay_time[1:])  # Ignore index 0
        return max_delay if max_delay < float('inf') else -1
