class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # num_dict = {}
        # for num in nums:
        #     num_dict[num] = num_dict.get(num, 0) + 1
        #     if num_dict[num] > 1:
        #         return True
        # return False

        visited_set = set()
        for n in nums:
            if n in visited_set:
                return True
            visited_set.add(n)
        return False