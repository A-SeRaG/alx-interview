#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Checks if placing a queen at board[row][col] is safe.

    Args:
        board (list): The current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Solves the N-Queens problem using backtracking.

    Args:
        n (int): The size of the board (NxN).
        row (int): The current row to place a queen.
        board (list): The current state of the board.
        solutions (list): The list to store all valid solutions.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
