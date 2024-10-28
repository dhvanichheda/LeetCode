class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ""
        word_list = s.split(' ')
        for i, w in enumerate(word_list):
            word_list[i] = self.reverseString(w)

        return " ".join(word_list)
        
    def reverseString(self, s: str) -> str:
        a = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l, r = l+1, r-1

        return "".join(a)

    