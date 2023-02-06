class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        num_len = len(nums)
        first_half = nums[0: (num_len // 2)] 
        second_half = nums[(num_len // 2):]
        shuffled_list = []
        for x,y in zip(first_half, second_half):
            shuffled_list.append(x)
            shuffled_list.append(y)

        return shuffled_list
