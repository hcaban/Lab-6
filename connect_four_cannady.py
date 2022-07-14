def initialize_board(height,length):
    board = []
    for i in range(height):
        row = []
        for j in range(length):
            row.append("-")
        board.append(row)
    return board


def print_board(board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            print(board[i][j], end=" ")
        print()


def check_if_winner(board, chip_type):
    count = 0
    # check all rows
    for i in range(row):
        for j in range(col):
            while board[i][j] == chip_type:
                count += 1
                if count >= 4:
                    return True

    # check all cols
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[2][j] == chip_type:
            return True

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == chip_type:
        return True
    if board[0][2] == board[1][1] == board[2][0] == chip_type:
        return True
    return False


def board_is_full(board):
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[0]):
            if board[i][j] == '-':
                return False
    return True


def is_valid(board, row, col):
    if -1 < row <= height + 1 and -1 < col <= length + 1 and board[row][col] == '-':
        return True
    return False


def available_square(board, row, col):
    return board[row][col] == '-'


def insert_chip(board, row, col, turn):
    if (turn + 1) % 2 == 0:
        board[row][col] = 'o'
    else:
        board[row][col] = 'x'



if __name__ == '__main__':
    height = int(input('What would you like the height of the board to be?'))
    length = int(input('What would you like the length of the board to be?'))
    board = initialize_board(height,length)

    print("Player 1: x\nPlayer 2: o")
    print_board(board)
    chip = 'x'
    player = ['Player 1', 'Player 2']
    row = height - 1
    old_col = 10000000
    count = 0
    turn = 1
    while True:
        turn = (turn + 1) % 2
        col = int(input(f"{player[turn]}: Which column would you like to choose? "))
        while not is_valid(board, row, col):
            if row < -1 or col < -1 or row > height - 1 or col > length - 1:
                print("This position is off the bounds of the board! Try again.")
            elif board[row][col] != '-' or old_col == col:
                row = row - 1
                insert_chip(board, row, col, turn)
                print_board(board)
                old_col = col
                count += 1
                if count > (height - 1):
                    count = 0
                    False
                    break
            turn = (turn + 1) % 2
            col = int(input(f"{player[turn]}: Which column would you like to choose? "))
        insert_chip(board, row, col, turn)
        print_board(board)
        #print()
        if check_if_winner(board, chip):
            if chip == 'x':
                print("Player 1 won the game!")
            else:
                print("Player 2 won the game!")
            break
        else:
            if board_is_full(board):
                print("Draw. Nobody wins.")
                break
        chip = 'o' if chip == 'x' else 'x'


