import numpy as np
import random

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if num == 0:
                print("X ", end="")
            else:
                print(f"{num} ", end="")
        print()

def generate_sudoku(difficulty):
    base = 3
    side = base * base

    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s))

    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * difficulty // 10
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

def solve_sudoku(board):
    def is_possible(board, y, x, n):
        for i in range(9):
            if board[y][i] == n or board[i][x] == n:
                return False
        x0, y0 = (x // 3) * 3, (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[y0 + i][x0 + j] == n:
                    return False
        return True

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(board, y, x, n):
                        board[y][x] = n
                        if solve_sudoku(board):
                            return True
                        board[y][x] = 0
                return False
    return True

def main():
    generated_board = None
    while True:
        print("\n============================")
        print("         Sudoku Menu        ")
        print("============================")
        print("1. Generate Sudoku")
        print("2. Solve Sudoku")
        print("3. Exit")
        print("============================")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n============================")
            print("      Select Difficulty     ")
            print("============================")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("============================")
            difficulty_choice = input("Enter your choice: ")
            if difficulty_choice == "1":
                difficulty = 4
            elif difficulty_choice == "2":
                difficulty = 6
            elif difficulty_choice == "3":
                difficulty = 8
            else:
                print("Invalid choice. Please select a valid difficulty.")
                continue
            generated_board = generate_sudoku(difficulty)
            print("\nGenerated Sudoku:")
            print_board(generated_board)
        
        elif choice == "2":
            if generated_board is not None:
                print("\n============================")
                print("  Solve the Sudoku Puzzle   ")
                print("============================")
                print("1. Solve the generated Sudoku")
                print("2. Input your own Sudoku")
                print("============================")
                solve_choice = input("Enter your choice: ")
                if solve_choice == "1":
                    board = generated_board
                elif solve_choice == "2":
                    board = []
                    print("Enter the Sudoku to solve (use 'X' or 'x' for empty spaces):")
                    for _ in range(9):
                        row = input().strip().split()
                        board.append([int(num) if num.upper() != 'X' else 0 for num in row])
                else:
                    print("Invalid choice. Please select a valid option.")
                    continue
            else:
                board = []
                print("Enter the Sudoku to solve (use 'X' or 'x' for empty spaces):")
                for _ in range(9):
                    row = input().strip().split()
                    board.append([int(num) if num.upper() != 'X' else 0 for num in row])
            print("Solving Sudoku...")
            if solve_sudoku(board):
                print("\nSolved Sudoku:")
                print_board(board)
            else:
                print("No solution exists for the given Sudoku.")
        
        elif choice == "3":
            print("Exiting program... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
