class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []

        num_set = set(nums)
        range_set = set()
        range_list = []
        cur_num = float("-inf")

        for i, num in enumerate(nums):
            
            if num <= cur_num:
                continue

            range_exist = False
            cur_num = num

            while num + 1 in num_set:
                range_exist = True
                num += 1

            # print(cur_num, num)

            if range_exist:
                range_list.append(f'{cur_num}->{num}')
                range_exist = False
                cur_num = num
            else:
                range_list.append(str(num))

        return range_list