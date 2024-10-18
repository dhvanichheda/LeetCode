class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return nums

        cons_set = set(nums)
        largest = 0
        for i in cons_set:
            if i-1 not in cons_set:
                curr = i
                curr_max = 1 

                while curr+1 in cons_set:
                    curr += 1
                    curr_max += 1
                
                largest = max(largest, curr_max)
                
        return largest
