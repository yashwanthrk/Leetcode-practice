class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort()


        merged_intervals = [intervals[0]]


        for index in range(1, len(intervals)):

        
            old_interval = merged_intervals[-1]

            if old_interval[1] >=  intervals[index][0]:

                start_time = min(old_interval[0], intervals[index][0])
                end_time = max(old_interval[1], intervals[index][1])
                merged_intervals.pop()
                merged_intervals.append((start_time, end_time))

            else:

                merged_intervals.append(intervals[index])


        return merged_intervals
                


