def validSolution(board):
    # check rows
    for row in board:
        # run through numbers 1 ~ 9 (range)
        for num in range(1, 10):
            # if number found in row**, then ok, if not, return false
            if num not in row:
                return False
    # check column
    transposed_board = list(map(list, zip(*board)))
    # print transposed_board
    for column in transposed_board:
        # run through numbers 1 ~ 9 (range)
        for num in range(1, 10):
        # if number found in column**, then ok, if not, return false
            if num not in column:
                return False
    # traversing grid
    for board_y in range(3):
        for board_x in range(3):
            temp_list = []
            for grid_y in range(3):
                for grid_x in range(3):
                    temp_list.append(board[grid_y + 3*board_y][grid_x + 3*board_x])
            for num in range(1, 10):
            # run through numbers 1 ~ 9 (range)
                if num not in temp_list:
                # if number found in grid, then ok, if not, return false
                    return False

    return True
print validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]])
