#!/usr/bin/python3
"""
N Queens Challenge

This script solves the N Queens problem using a backtracking algorithm. The
N Queens problem is the challenge of placing N chess queens on an N×N
chessboard so that no two queens threaten each other.

Usage:
    nqueens N

Arguments:
    N: The size of the chessboard (N x N) and the number of queens to place.
       N must be an integer greater than or equal to 4.

Example:
    ./nqueens.py 8
"""

import sys


def is_safe(placed_queens, row, col):
    """
    Check if placing a queen at (row, col) is safe.

    Args:
        placed_queens (list): List of coordinates where queens are placed.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for r, c in placed_queens:
        if c == col or c + (row - r) == col or c - (row - r) == col:
            return False
    return True


def solve_n_queens(n):
    """
    Solve the N Queens problem.

    Args:
        n (int): The size of the chessboard (N x N) and the number of queens.

    Returns:
        list: A list of solutions, where each solution is represented as a list
              of coordinates [row, column].
    """
    solutions = []
    placed_queens = []
    stop = False
    r = 0
    c = 0

    while r < n:
        goback = False
        while c < n:
            if is_safe(placed_queens, r, c):
                placed_queens.append([r, c])
                if r == n - 1:
                    solutions.append(placed_queens[:])
                    for cord in placed_queens:
                        if cord[1] < n - 1:
                            r = cord[0]
                            c = cord[1]
                    for i in range(n - r):
                        placed_queens.pop()
                    if r == n - 1 and c == n - 1:
                        placed_queens = []
                        stop = True
                    r -= 1
                    c += 1
                else:
                    c = 0
                break
            else:
                if c == n - 1:
                    goback = True
                    break
                c += 1

        if stop:
            break

        if goback:
            r -= 1
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_n_queens(n)

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)


if __name__ == '__main__':
    main()
