class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        longest_len = 1
        longest = s[0]

        for idx in range(len_s):
            # odd length
            l, r = idx - 1, idx + 1
            curr_len = 1
            curr_str = ""
            while l >= 0 and r < len_s and s[l] == s[r]:
                curr_len += 2
                curr_str = s[l:r+1]
                l, r = l - 1, r + 1
            
            if longest_len < curr_len:
                longest = curr_str
                longest_len = curr_len

            # even length 
            l, r = idx, idx + 1
            curr_len = 0
            while  l >= 0 and r < len_s and s[l] == s[r]:
                curr_len += 2
                curr_str = s[l:r+1]
                l, r = l - 1, r + 1

            if longest_len < curr_len:
                longest = curr_str
                longest_len = curr_len

        return longest 

    


    