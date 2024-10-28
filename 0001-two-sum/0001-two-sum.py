class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in num_map:
                return [i, num_map[comp]]
            else:
                num_map[v] = i 

        return []