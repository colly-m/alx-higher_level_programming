#!/usr/bin/python3
"""The chess N-queens puzzle"""

import sys


def getz_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_copy(board):
    """Returns a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def getz_lists(board):
    """Returns the list of lists representation in a board."""
    lists = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                lists.append([r, c])
                break
    return (lists)


def xout(board, row, clmn):
    """X spots on a chessboard"""
    # X out all forward spots
    for c in range(clmn + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(clmn - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][clmn] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][clmn] = "x"
    # X out all spots diagonally down to the right
    c = clmn + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = clmn - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = clmn + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = clmn - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_output(board, row, queens, lists):
    """Recursively solves an N-queens puzzle"""
    if queens == len(board):
        lists.append(getz_lists(board))
        return (lists)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            lists = recursive_output(tmp_board, row + 1,
                                        queens + 1, lists)

    return (lists)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = getz_board(int(sys.argv[1]))
    lists = recursive_output(board, 0, 0, [])
    for answer in lists:
        print(answer)
