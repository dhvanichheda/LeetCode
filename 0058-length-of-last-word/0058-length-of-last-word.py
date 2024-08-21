class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_string = s.strip().split(" ")
        return len(split_string[-1])