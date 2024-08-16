from string import ascii_letters, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        #convert all to lowercase and remove all non-alphanumeric characters
        s = "".join([c for c in s if c in (ascii_letters + digits)])
        s = s.lower()
        if (len(s) == 1) or s == "":
            return True 
 
        #start traversing from front and back and compare. Stop at the mid point 
        start_idx = 0 
        end_idx = len(s) - 1
        while start_idx < end_idx:
            if s[start_idx] != s[end_idx]:
                return False 
            start_idx += 1
            end_idx -= 1

        return True

