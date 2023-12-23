class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        new_arr = [intervals[0]]

        for i in range(1, len(intervals)):
            if new_arr[-1][1] >= intervals[i][0]:
                
                # important line
                new_arr[-1][1] = max(new_arr[-1][1], intervals[i][1])
                # print(new_arr[-1][1])
            else:
                new_arr.append(intervals[i])

        return new_arr