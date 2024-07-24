from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        for time, val in reversed(values):
            if time <= timestamp:
                return val

        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)