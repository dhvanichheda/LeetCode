'''play with index - 
    1. start with 0 till you reach the end 
    2. go through last of all 
    3. decrement back to 0 
    4. go through 0 of all 
    5. now repeat by decrementing last and increment 0
    6. end the loop when curr index count equals total number of elements 
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output_list = []

        total_elements = len(matrix[0]) * len(matrix)
        num_lists = len(matrix)
        curr_list = 0
        head_idx = top_idx = curr_idx = 0 
        tail_idx = len(matrix[0]) - 1
        bottom_idx = num_lists - 1
        compl_elem = 0

        while compl_elem <= total_elements:
            while curr_idx <= tail_idx:
                output_list.append(matrix[curr_list][curr_idx])
                curr_idx += 1
                compl_elem += 1

            if compl_elem == total_elements:
                break
            curr_list += 1
            top_idx += 1
            curr_idx -= 1
            while curr_list <= bottom_idx:
                output_list.append(matrix[curr_list][curr_idx])
                curr_list += 1
                compl_elem += 1

            if compl_elem == total_elements:
                break
            tail_idx -= 1
            curr_list -= 1
            curr_idx -= 1 
            while curr_idx >= head_idx:
                output_list.append(matrix[curr_list][curr_idx])
                curr_idx -= 1
                compl_elem += 1

            if compl_elem == total_elements:
                break
            bottom_idx -= 1
            curr_list -= 1
            curr_idx += 1
            while curr_list >= top_idx:
                output_list.append(matrix[curr_list][curr_idx])
                curr_list -= 1
                compl_elem += 1

            if compl_elem == total_elements:
                break
            head_idx += 1
            curr_list += 1
            curr_idx += 1

        return output_list  

