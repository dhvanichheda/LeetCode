class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True 
        elif len(t) == 0:
            return False 

        t_idx = 0
        found_c = 1
        new_str = ""
        for c in s:
            if found_c != 1:
                return False 
            found_c = 0
            for t_idx in range(t_idx, len(t)):
                if c == t[t_idx]:
                    t_idx += 1
                    new_str += c
                    found_c = 1
                    break

        if s == new_str:
            return True 

        return False 