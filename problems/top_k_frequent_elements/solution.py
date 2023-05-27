from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        

        # Sorted parameters are as follows sorted(iterable, key, reverse=?) where iterable is what you wanna iterate through, key is the function you wanna apply, and reverse=True sorts in decreasing order. 
        # So in this case the iterable will be d.items() which is in the tuple format, key is a lambda fucntion lambda x:x[1], which is telling the sort to happen in terms of the values and reverse=True to sort in a decending order.
        sorted_nums = sorted(num_counter.items(), key=lambda item: item[1], reverse = True)
        return [sorted_nums[i][0] for i in range(k)]
		
       
      
                