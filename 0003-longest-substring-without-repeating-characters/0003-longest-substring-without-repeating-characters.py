class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx_map = {}
        l = r = 0
        longest = 0  

        while r < len(s):
            curr = s[r]
            if curr in idx_map and idx_map[curr] >= l:
                l = idx_map[curr] + 1
                idx_map[curr] = r
            else:
                idx_map[curr] = r

            longest = max(longest, r - l + 1)
            r += 1

        return longest 



