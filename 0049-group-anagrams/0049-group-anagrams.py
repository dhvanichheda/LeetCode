class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            if strs[0] == "":
                return [[""]]
            else:  
                return [strs[0]]

        #1. sort letters of each str 
        #2. create dict with sorted str as key and list of anagrams as values
        sorted_words_map = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in sorted_words_map:
                sorted_words_map[ss].append(s)
            else:
                sorted_words_map[ss] = [s]

        output_list = []
        for v in sorted_words_map.values():
            output_list.append(v)

        return output_list
