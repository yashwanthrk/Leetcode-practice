class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
       # Step 1: Sort intervals by start times
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev = result[-1]  # Last interval in result
            current = intervals[i]
            
            if prev[1] >= current[0]: 
                prev[1] = max(prev[1], current[1])
            else:
                # No overlap, add current interval to result
                result.append(current)
        
        return result