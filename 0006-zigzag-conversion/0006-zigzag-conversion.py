class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        n = len(s)
        if num_rows == 1 or n == num_rows:
            return s

        num_cols = 1
        sum_c = num_rows
        while sum_c <= n:
            sum_c += (num_rows - 2)
            num_cols += (num_rows - 2)
            if sum_c > n:
                break
            else:
                sum_c += num_rows
                num_cols += 1

        #char_mat = [[""] * num_cols] * num_rows
        char_mat = [["" for _ in range(num_cols)] for _ in range(num_rows)]
        r = -1
        c = 0
        s_idx = 0 
        while s_idx < n:
            for i in range(num_rows):
                if s_idx >= n:
                    break
                r += 1
                char_mat[r][c] = s[s_idx]
                s_idx += 1 
            

            for i in range(num_rows - 2):
                if s_idx >= n:
                    break
                r -= 1
                c += 1
                char_mat[r][c] = s[s_idx]
                s_idx += 1

            r -= 2
            c += 1


        result_str = ""
        for i in range(len(char_mat)):
            for j in range(len(char_mat[i])):
                c = char_mat[i][j]
                if c != "":
                    result_str += c

        return result_str
