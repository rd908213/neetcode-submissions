class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This section checks the rows and columns
        for i in range(9):
            col_chk = [0] * 9
            row_chk = [0] * 9
            for j in range(9):
                # board[i][j] refers to row i, column j
                if board[i][j] in col_chk and board[i][j] != '.':
                    print(f"col_chk: {col_chk}")
                    return False
                else:
                    col_chk[j] = (board[i][j]) # Go down a column and check if a value is already present

                # board[j][i] refers to row j, column i
                if board[j][i] in row_chk and board[j][i] != '.':
                    print(f"row_chk: {row_chk}")
                    return False
                else:
                    row_chk[j] = (board[j][i]) # Go down a row and check if a value is already present
        
        # This section checks the cells
        for i in range(3): # Traverse the cells up and down
            center_x = 3 * i + 1
            for j in range(3): # Traverse the cells left to right
                center_y = 3 * j + 1
                cell_chk = [0] * 9 # cell_chk is a flattened version of the row
                for x in range(center_x - 1, center_x + 2):
                    for y in range(center_y - 1, center_y + 2):
                        if board[x][y] in cell_chk and board[x][y] != '.':
                            return False
                        else:
                            cell_chk[3 * (x % 3) + y % 3] = board[x][y]
                            # Modulo is used to get relative cell coordinates
                            # the x coordinate is multiplied by 3 to signify that 3 cells have been checked
                print(cell_chk)
        return True

