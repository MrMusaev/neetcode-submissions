class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sub_box_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                row_set = row_sets[i]
                col_set = col_sets[j]
                sub_box_set = sub_box_sets[i // 3][j // 3]

                if num in row_set:
                    return False
                
                if num in col_set:
                    return False
                
                if num in sub_box_set:
                    return False

                row_set.add(num)
                col_set.add(num)
                sub_box_set.add(num)
        
        return True