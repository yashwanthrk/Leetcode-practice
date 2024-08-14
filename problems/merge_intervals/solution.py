class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

       # Sort intervals by the starting point
        intervals = sorted(intervals, key=lambda x: x[0])

        merged_intervals = [intervals[0]]
        
        for index in range(1, len(intervals)):
            
            current_interval = intervals[index]
            last_merged_interval = merged_intervals[-1]

            if last_merged_interval[1] >= current_interval[0]:
                # Merge them by updating the end of the last merged interval
                last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
            else:
                merged_intervals.append(current_interval)
        
        return merged_intervals