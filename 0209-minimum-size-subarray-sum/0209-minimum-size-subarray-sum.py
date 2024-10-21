# Sliding window approach 
'''
1. Keep left and right index pointers to represent windows
2. Keep expanding right pointer till the sum is greater than target. Increment min_window size. 
3. Once greater or equal, subtract the left pointer value from sum. Increment left pointer. Decrement min_window size.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        shortest = float('inf')
        
        for r in range(0, len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                shortest = min(shortest, r-l+1)
                curr_sum -= nums[l]
                l += 1
                
        return shortest if shortest != float('inf') else 0