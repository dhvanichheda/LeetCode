class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        output_list = []

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]

        for k in anagram_map:
            output_list.append(anagram_map[k])

        return output_list