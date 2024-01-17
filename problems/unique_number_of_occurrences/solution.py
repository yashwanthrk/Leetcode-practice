class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        occurences = {}

        for num in arr:
           occurences[num] =  occurences.get(num, 0) + 1

        
        duplicate = set()
        for key, value in occurences.items():
            if value in duplicate:
                return False
            duplicate.add(value)
        return True


        