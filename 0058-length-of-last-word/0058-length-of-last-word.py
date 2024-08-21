class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_split = s.strip().split(" ")
        return len(str_split[-1].strip())