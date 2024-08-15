class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        modified_intervals = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            modified_intervals.append(intervals[i])

            i += 1
        
        # Merge intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        modified_intervals.append(newInterval)
        
        while i < n:
            modified_intervals.append(intervals[i])
            i += 1
        
        return modified_intervals