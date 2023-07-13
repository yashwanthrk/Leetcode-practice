import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.num_map:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.num_map:
            idx = self.num_map[val]
            last_val = self.num_list[-1]
            
            # Swap last value with value to be removed, so we can remove in O(1)
            self.num_list[idx], self.num_list[-1] = self.num_list[-1], self.num_list[idx]
            
            self.num_map[last_val] = idx
            self.num_list.pop()
            del self.num_map[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.num_list)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()