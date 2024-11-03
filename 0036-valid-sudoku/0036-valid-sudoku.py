'''
1. Maintain a list of hash sets for rows, columns and boxes
2. Example - 
   row_list = [{5,3,.,.}, {6,.,.,1}, {., 9,8}]
   column_list = [{5,6,.}, {3,.,9}, {.,.,8}]
   box_list = [{5,3,.,6}, {.,7,.,1}, {.,.,.}]
3. Identify box number with logic - (r/3) * 3 + (c/3) 
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = [set() for _ in range(9)]
        column_list = [set() for _ in range(9)]
        box_list = [set() for _ in range(9)]

        for r in range(0, 9):          
            for c in range(0, 9):
                if board[r][c] != '.':
                    if board[r][c] not in row_list[r]:
                        row_list[r].add(board[r][c]) 
                    else: 
                        return False   

                    if board[r][c] not in column_list[c]:
                        column_list[c].add(board[r][c])
                    else:
                        return False

                    box_idx = (r//3)*3 + (c//3)
                    if board[r][c] not in box_list[box_idx]: 
                        box_list[box_idx].add(board[r][c])
                    else:
                        return False

        return True