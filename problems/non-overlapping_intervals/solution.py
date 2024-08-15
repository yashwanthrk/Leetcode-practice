class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        # Sort intervals by the ending time to optimize the number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])
       
        prev_end = intervals[0][1]

        print(intervals)
        minimum_count = 0

        for start, end in intervals[1:]:
            
            # not overlaping 
            if start >= prev_end:
                prev_end = end

            else:
                minimum_count += 1
                prev_end = min(end, prev_end)

        return minimum_count
