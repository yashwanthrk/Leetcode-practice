class TimeMap:

    def __init__(self):
        # key : list of [value, timestamp]
        self.key_time_map = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_time_map:
            self.key_time_map[key] = []
        
        self.key_time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_time_map.get(key, [])

        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:

                # Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns ""
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res



       


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)