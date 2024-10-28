class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1] # Python slicing handles out-of-range indices gracefully. So if i+k is beyond the string length, it will only consider the slice up to the end of the string 

        return "".join(a)

        

             

