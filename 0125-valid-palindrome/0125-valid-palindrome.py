class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_phrase = ""
        for c in s.lower():
            if c.isalnum():
                clean_phrase += c

        i, j = 0, len(clean_phrase) - 1
        while i < j:
            if clean_phrase[i] != clean_phrase[j]:
                return False 

            i += 1
            j -= 1

        return True
        