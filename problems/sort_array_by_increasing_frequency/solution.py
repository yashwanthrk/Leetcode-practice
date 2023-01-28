class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # counter = collections.Counter(nums)
        # nums = sorted(nums, key=lambda x: (counter[x], -x))
        # return nums

            
        # sorted(nums, key=lambda x: (r[x], -x)) 
        # is sorting a list nums based on a lambda function that takes an input x and returns a tuple (r[x], -x). The sorted function sorts the list based on the first element of the tuple in ascending order, and if two elements have the same value for the first element of the tuple, it will sort them based on the second element of the tuple in descending order.

        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        heap_items = []
        for key, val in count_dict.items():
            heapq.heappush(heap_items,[val, -key])

        output = []
        while(heap_items):
            val, negative_key = heapq.heappop(heap_items)
            for i in range(val):
                output.append( negative_key * (-1) )

        return(output)




        






