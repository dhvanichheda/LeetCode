class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for idx, val in enumerate(nums):
            compliment = target - nums[idx]
            if target - val in idx_map:
                return [idx, idx_map[compliment]]
            else:
                idx_map[val] = idx

        return []