from queue import Queue

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        str_set = set()
        curr_len = 0
        l = 0
        for c in s:
            if c in str_set:
                if curr_len > longest:
                    longest = curr_len
                while s[l] != c:
                    str_set.remove(s[l])
                    l += 1
                    curr_len -= 1
                l += 1
            else:
                str_set.add(c)
                curr_len += 1

        return max(longest, curr_len)                
