import time
from copy import deepcopy

black_square = [['█' for i in range(9)] for j in range(5)]
white_square = [[' ' for i in range(9)] for j in range(5)]
black_queen = [[None for i in range(9)] for j in range(5)]
white_queen = [[None for i in range(9)] for j in range(5)]

for i in range(5):
    for j in range(9):
        if i == 0 or i == 4:
            white_queen[i][j] = " "
            black_queen[i][j] = "█"
        elif j <=  1 or j > 6:
            white_queen[i][j] = " "
            black_queen[i][j] = "█"
        elif i ==  1 and (j == 3 or j == 5):
            white_queen[i][j] = " "
            black_queen[i][j] = "█"
        else:
            white_queen[i][j] = "█"
            black_queen[i][j] = " "

def test(queens, size, row, col):
    for c in range(0, col):
        if queens[c] == row:
            return False

    i = 1
    while row - i >= 0 and col - i >= 0:
        if row - i == queens[col - i]:
            return False
        i += 1

    i = 1
    while row + i < size and col - i >= 0:
        if row + i == queens[col - i]:
            return False
        i += 1

    return True

def _make_board(size):
    board = deepcopy(empty_board)

    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                if queens[i] == j:
                    board[i][j] = white_queen
                else:
                    board[i][j] = white_square
            else:
                if queens[i] == j:
                    board[i][j] = black_queen
                else:
                    board[i][j] = black_square
    return board

def print_board(size):
    board = _make_board(size)

    print()
    print('_' * 9 * size)

    for i in range(size):
        for k in range(5):
            print('|', end='')
            for j in range(size):
                for l in range(9):
                    print(board[i][j][k][l], end='')
            print('|')

    print('_' * 9 * size)
    print()

def solve(queens, size):
    row = 0
    col = 0
    solution = 0

    while col >= 0:
        if (col == size or row == size):
            col -= 1
            if col < 0:
                print('Number of solutions found', solution, '\n')
                break
            row = queens[col]
            queens[col] = 0
            row += 1
            continue

        if test(queens, size, row, col):
            queens[col] = row
            row = 0
            col += 1
            if col == size:
                solution += 1
                print('Solution #', solution)
                print_board(size)
                print()
        else:
            row += 1

    return None


if __name__ == '__main__':
    size = int(input('Enter size: '))
    queens = [0 for _ in range(size)]
    empty_board = [[None for i in range(size)] for j in range(size)]

    t1 = time.time()
    solve(queens, size)
    t2 = time.time()
    
    print(t2 - t1)
