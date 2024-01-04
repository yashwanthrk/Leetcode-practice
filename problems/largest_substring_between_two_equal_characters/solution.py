class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """

        indices_map = {}

        for index, num in enumerate(s):
            if num in indices_map:
                indices_map[num].append(index)
            else:
                indices_map[num] = [index]
        
        max_gap = -1
        for num, gap in indices_map.items():
            small = min(gap)
            large = max(gap)
            max_gap = max(max_gap, large - small - 1)
        
        return max_gap 

        

