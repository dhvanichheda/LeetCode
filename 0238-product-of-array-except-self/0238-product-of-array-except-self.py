class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = [1] * len(nums)
        for idx in range(1,len(nums)):
            prod_list[idx] = prod_list[idx-1] * nums[idx-1]

        prod = 1
        for idx in range(len(nums)-2, -1, -1):
            prod = prod * nums[idx+1]
            prod_list[idx] = prod_list[idx] * prod

        return prod_list