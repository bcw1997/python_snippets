"""
Create a minesweeper game using arrays/
bombs = list of bomb locations 
rows, columns 
mine_sweeper([0,0], [1,2], 3, 4)

bomb at row index 0 | column index 0
bomb at row index 0 | column index 1
3 rows
4 cols

Return an 3x4 array (-1) = bomb
"""


def mine_sweeper(bombs, num_rows, num_cols):
    board = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    for bomb_loc in bombs: 
        (bomb_row, bomb_col) = bomb_loc
        board[bomb_row][bomb_col] = -1
        
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)
        
        #iterating in a top-to-bottom, left-to-right manner
        for i in row_range:
            current_i = i 
            for j in col_range:
                current_j = j
                if (0 <= i < num_rows and 0 <= j < num_cols and board[i][j] != -1): # if >= 0 for row & cols & no bomb (-1), update to +1 
                    board[i][j] += 1
    return board
    
print(mine_sweeper([[0,0],[1,2]],3,4))
    
