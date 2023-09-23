class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        tree_map = {}
        max_count = 0
        left = 0
        
        for right, fruit in enumerate(fruits):
            tree_map[fruit] = tree_map.get(fruit, 0) + 1

            while len(tree_map) > 2:

                tree_map[fruits[left]] -= 1

                if tree_map[fruits[left]] ==  0:
                    del tree_map[fruits[left]]
                
                # shrink
                left += 1
                
            max_count = max(max_count, right - left + 1)
        
        return max_count

