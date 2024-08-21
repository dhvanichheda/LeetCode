class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True 
        elif len(t) == 0:
            return False 

        char_map = {}
        for c in t:
            char_map[c] = char_map.get(c, 0) + 1

        for c in s:
            if c in char_map:
                char_map[c] -= 1
            else:
                return False
    
        return True 