class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        

        events = []

        for passenger, st_time, end_time in trips:
            events.append([st_time, passenger])
            events.append([end_time, -passenger])
        
        events.sort()

        curr_capacity = 0

        for time, passenger_count in events:
            curr_capacity += passenger_count
            if curr_capacity > capacity:
                return False

        return True 