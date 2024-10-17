class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)
        if nums_len == 1 or k == 0 or k == nums_len:
            return nums 

        while k > nums_len:
            k = k - nums_len
        k_list = nums[(nums_len - k):]
        repl_idx = nums_len - 1
        for i in range((nums_len - k - 1), -1, -1):
            nums[repl_idx] = nums[i]
            repl_idx -= 1

        for i in range(0, k):
            nums[i] = k_list[i]

        return nums

        