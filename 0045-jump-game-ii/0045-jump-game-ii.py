# Check your jump options from starting point 
# Select the option that will allow you to make the biggest jump
# Continue doing this - check options and select one that allows you the maximum jump 

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        jumps = 0
        l = r = 0

        while r < (len(nums) - 1):
            farthest = 0 
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1

        return jumps