'''
1. Find number of unique characters and their occurence index (store in a dict) for both strings 
2. If both match, return True, else False 
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return True 

        s_map = {}
        for idx, c in enumerate(s):
            if c in s_map:
                s_map[c].append(idx)
            else:
                s_map[c] = [idx]

        t_map = {}
        for idx, c in enumerate(t):
            if c in t_map:
                t_map[c].append(idx)
            else:
                t_map[c] = [idx] 

        for l in s_map.values():
            for k, v in t_map.items():
                if l == v:
                    t_map.pop(k)
                    break

        if len(t_map) == 0:
            return True
        else:
            return False 