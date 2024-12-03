class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        # Step 1: Sort intervals by start time
        intervals.sort()

        merged_intervals = [intervals[0]]

        for index in range(1, len(intervals)):
            
            prev_interval = merged_intervals[-1]

            # If the current interval overlaps with the previous one
            if intervals[index][0] <= prev_interval[1]:
                new_start_time =  min(prev_interval[0], intervals[index][0])
                new_end_time = max(prev_interval[1], intervals[index][1])
                merged_intervals[-1] = [new_start_time, new_end_time]
            else:
                merged_intervals.append(intervals[index])

        return merged_intervals