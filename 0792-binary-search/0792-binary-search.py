class Solution:
    def search(self, nums: List[int], target: int) -> int:
        curr_len = len(nums)
        r = curr_len - 1
        idx = int(curr_len/2)
        print(f'idx = {idx}')
        while curr_len > 0:
            if nums[idx] < target:
                curr_len = r - idx
                idx += (1 if curr_len == 1 else int(curr_len/2)) 
            elif nums[idx] > target:
                r = idx - 1
                curr_len = idx
                idx = int(curr_len/2)
            else:
                return idx


        return -1