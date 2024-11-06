class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        non_zero_idx = 0 

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        
        while non_zero_idx < len(nums):
            nums[non_zero_idx] = 0
            non_zero_idx += 1
            